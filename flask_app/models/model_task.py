from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re
import os
from dotenv import load_dotenv
load_dotenv(override=True)

DATABASE = os.environ.get('DB_NAME')


class Task:
    def __init__(self, data):
        self.id = data['id']
        self.category = data['category']
        self.description = data['description']
        self.status = data['status']
        self.due_date = data['due_date']
        self.user_id = data['user_id']
        self.team_id = data['team_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.first_name = data['first_name']
        self.last_name = data['last_name']

    @classmethod
    def get_all_user_tasks(cls, data):
        query = "SELECT tasks.id, tasks.category, tasks.description, tasks.status, tasks.due_date, tasks.user_id, tasks.team_id, tasks.created_at, tasks.updated_at, users.first_name, users.last_name FROM tasks LEFT JOIN users ON tasks.user_id = users.id WHERE tasks.team_id = %(team_id)s AND tasks.user_id = %(id)s ORDER BY tasks.due_date ASC;"
        result = connectToMySQL(DATABASE).query_db(query, data)

        if result:
            all_user_tasks = []
            for task in result:
                all_user_tasks.append(cls(task))
            return all_user_tasks

        return None

    @classmethod
    def get_all_team_tasks(cls, data):
        query = "SELECT tasks.id, tasks.category, tasks.description, tasks.status, tasks.due_date, tasks.user_id, tasks.team_id, tasks.created_at, tasks.updated_at, users.first_name, users.last_name FROM tasks LEFT JOIN users ON tasks.user_id = users.id WHERE tasks.team_id = %(team_id)s AND tasks.category = 'Public' ORDER BY tasks.due_date ASC;"
        result = connectToMySQL(DATABASE).query_db(query, data)

        if result:
            all_team_tasks = []
            for task in result:
                all_team_tasks.append(cls(task))
            return all_team_tasks

        return None

    @classmethod
    def get_one_task_by_task_id(cls, data):
        query = "SELECT tasks.id, tasks.category, tasks.description, tasks.status, tasks.due_date, tasks.user_id, tasks.team_id, tasks.created_at, tasks.updated_at, users.first_name, users.last_name FROM tasks LEFT JOIN users ON tasks.user_id = users.id WHERE tasks.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)

        if result:
            return cls(result[0])

        return None

    @classmethod
    def create_task(cls, data):
        query = "INSERT INTO tasks (category, description, status, due_date, user_id, team_id) VALUES (%(category)s, %(description)s, %(status)s, %(due_date)s, %(user_id)s, %(team_id)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def update_task(cls, data):
        query = "UPDATE tasks SET category = %(category)s, description = %(description)s, status = %(status)s, due_date = %(due_date)s WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def delete_task(cls, data):
        query = "DELETE FROM tasks WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @staticmethod
    def validate_task(data):
        is_valid = True

        if not data['category']:
            flash('Please select category.', 'error_task_category')
            is_valid = False

        if len(data['description']) < 1:
            flash('Please enter description.', 'error_task_description')
            is_valid = False

        if not data['status']:
            flash('Please select status.', 'error_task_status')
            is_valid = False

        if not data['due_date']:
            flash('Please select due date.', 'error_task_due_date')
            is_valid = False

        return is_valid
