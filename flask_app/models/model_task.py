from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_user import User
import re
import os
from dotenv import load_dotenv
load_dotenv(override=True)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATABASE = os.environ.get('DB_NAME')


class Task:
    def __init__(self, data):
        self.id = data['id']
        self.category = data['category']
        self.description = data['description']
        self.status = data['status']
        self.due_date = data['due_date']
        self.assignee_id = data['assignee_id']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO tasks (category, description, status, due_date, assignee_id, user_id) VALUES (%(category)s, %(description)s, %(status)s, %(due_date)s, %(assignee_id)s, %(user_id)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_one_task_by_task_id(cls, data):
        query = "SELECT * FROM tasks LEFT JOIN users ON tasks.user_id = users.id WHERE tasks.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            current_task = cls(result[0])
            user_data = {
                **result[0],
                "created_at": result[0]['users.created_at'],
                "updated_at": result[0]['users.updated_at'],
                "id": result[0]['users.id']
            }
            current_task.user = User(user_data)
            return current_task
        else:
            return None

    @classmethod
    def get_all_tasks_by_user(cls, data):
        query = "SELECT * FROM tasks LEFT JOIN users ON tasks.assignee_id = users.id WHERE users.id= %(id)s ORDER BY due_date ASC;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        all_tasks = []
        for task in result:
            all_tasks.append(cls(task))
        return all_tasks

    @classmethod
    def get_all_public_tasks_by_team(cls, data):
        query = "SELECT * FROM tasks JOIN users ON users.id = tasks.user_id JOIN teams ON users.team_id = teams.id WHERE teams.id = %(id)s AND tasks.category = %(category)s ORDER BY due_date ASC;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def update_one(cls, data):
        query = "UPDATE tasks SET category = %(category)s, description = %(description)s, %(status)s, due_date = %(due_date)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM tasks WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_tasks(data):
        is_valid = True

        if not data['category']:
            flash('Field is required.', 'err_add_task_category')
            is_valid = False

        if len(data['description']) < 1:
            flash('Field is required.', 'err_add_task_description')
            is_valid = False

        if not data['due']:
            flash('Field is required.', 'err_add_task_due')
            is_valid = False

        return is_valid
