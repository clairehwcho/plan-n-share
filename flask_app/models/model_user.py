from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import bcrypt
from flask import flash, session
import re
import os
from dotenv import load_dotenv
load_dotenv(override=True)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATABASE = os.environ.get('DB_NAME')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.team_id = data['team_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one_user_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def get_all_users_by_team_id(cls, data):
        query = 'SELECT * FROM users LEFT JOIN teams ON users.team_id = teams.id WHERE users.team_id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        all_team_users = []
        for user in result:
            all_team_users.append(cls(user))
        return all_team_users

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password, team_id) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(team_id)s);'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def update(cls, data):
        query = 'UPDATE users SET team_id = %(team_id)s WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_register(data):
        is_valid = True

        if len(data['first_name']) < 2:
            flash('Please enter your first name.', 'error_register_first_name')
            is_valid = False

        if len(data['last_name']) < 2:
            flash('Please enter your last name', 'error_register_last_name')
            is_valid = False

        if len(data['email']) < 1:
            flash('Please enter your email.', 'error_register_email')
            is_valid = False

        elif not EMAIL_REGEX.match(data['email']):
            flash('Invalid email format', 'error_register_email')
            is_valid = False

        else:
            existing_email = User.get_one_user_by_email(
                {'email': data['email']})
            if existing_email:
                flash('This email is already in use.', 'error_register_email')
                is_valid = False

        if len(data['password']) < 1:
            flash('Please enter your password.', 'error_register_password')
            is_valid = False

        if len(data['confirm_password']) < 1:
            flash('Please confirm your password.', 'error_register_confirm_password')
            is_valid = False

        elif data['password'] != data['confirm_password']:
            flash('Passwords do not match.', 'error_register_confirm_password')
            is_valid = False

        if len(data['team_id']) < 1:
            flash('Please select your team', 'error_register_team_id')
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True

        if len(data['email']) < 1:
            flash('Please enter your email.', 'error_login_email')
            is_valid = False

        elif not EMAIL_REGEX.match(data['email']):
            flash('Invalid email format', 'error_login_email')
            is_valid = False

        else:
            existing_email = User.get_one_user_by_email(
                {'email': data['email']})
            if not existing_email:
                flash('Invalid credentials', 'error_login_email')
                is_valid = False
            elif not bcrypt.check_password_hash(existing_email.password, data['password']):
                flash('Invalid credentials', 'error_login_password')
                is_valid = False
            else:
                session['current_user'] = existing_email.id

        if len(data['password']) < 1:
            flash('Please enter your password.', 'error_login_password')
            is_valid = False

        return is_valid
