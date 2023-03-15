from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
import re
import os
from dotenv import load_dotenv
load_dotenv()

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATABASE = os.environ.get('DB_NAME')

class Team:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO teams (name) VALUES (%(name)s);'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def get_all_teams(cls):
        query = 'SELECT * FROM teams;'
        result = connectToMySQL(DATABASE).query_db(query)
        all_teams = []
        for row in result:
            all_teams.append( cls(row) )
        return all_teams

    @classmethod
    def get_one_id_by_name(cls, data):
        query = 'SELECT * FROM teams WHERE name = %(name)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return None

    @classmethod
    def get_one_team_by_user(cls, data):
        query = 'SELECT * FROM teams JOIN users on teams.id = users.team_id WHERE users.id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return None

    @staticmethod
    def validate_create_team(data):
        is_valid = True

        if len(data['name']) < 1:
            flash('Field is required.', 'err_add_team')
            is_valid = False

        return is_valid

    @staticmethod
    def validate_join_team(data):
        is_valid = True

        if not data['name']:
            flash('Field is required.', 'err_join_team')
            is_valid = False

        return is_valid