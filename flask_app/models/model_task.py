from flask import flash
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
        self.creator_first_name = data['creator_first_name']
        self.creator_last_name = data['creator_last_name']
        self.assignee_first_name = data['assignee_first_name']
        self.assignee_last_name = data['assignee_last_name']

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
            current_task['user'] = User(user_data)
            return current_task
        else:
            return None

    @classmethod
    def get_all_user_tasks_by_user_id(cls, data):
        query = "SELECT  tasks.id, tasks.category, tasks.description, tasks.status, tasks.due_date, tasks.assignee_id, tasks.user_id, tasks.created_at, tasks.updated_at, creators.first_name AS creator_first_name, creators.last_name AS creator_last_name, assignees.first_name AS assignee_first_name, assignees.last_name AS assignee_last_name FROM tasks LEFT JOIN users AS creators ON tasks.user_id = creators.id LEFT JOIN users AS assignees ON tasks.assignee_id = assignees.id WHERE tasks.assignee_id = %(id)s ORDER BY tasks.due_date ASC;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        all_user_tasks = []
        for task in result:
            all_user_tasks.append(cls(task))
        return all_user_tasks

    @classmethod
    def get_all_team_tasks_by_team_id(cls, data):
        query = "SELECT tasks.id, tasks.category, tasks.description, tasks.status, tasks.due_date, tasks.assignee_id, tasks.user_id, tasks.created_at, tasks.updated_at, creators.first_name AS creator_first_name, creators.last_name AS creator_last_name, assignees.first_name AS assignee_first_name, assignees.last_name AS assignee_last_name from tasks LEFT JOIN users AS creators ON tasks.user_id = creators.id LEFT JOIN users AS assignees ON tasks.assignee_id = assignees.id LEFT JOIN teams ON creators.team_id = teams.id WHERE teams.id = %(id)s AND tasks.category = 'Public' ORDER BY tasks.due_date ASC;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        all_team_tasks = []
        for task in result:
            all_team_tasks.append(cls(task))
        return all_team_tasks

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
            flash('Please select category.', 'error_add_tasks_category')
            is_valid = False

        if len(data['description']) < 1:
            flash('Please enter description.', 'error_add_tasks_description')
            is_valid = False

        if not data['status']:
            flash('Please select status.', 'error_add_tasks_status')
            is_valid = False

        if not data['due_date']:
            flash('Please select due date.', 'error_add_tasks_due_date')
            is_valid = False

        if not data['assignee_id']:
            flash('Please select assignee.', 'error_add_tasks_assignee_id')
            is_valid = False

        return is_valid
