from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE = os.environ.get('DB_NAME')


class Team:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_teams(cls):
        query = "SELECT * FROM teams;"
        result = connectToMySQL(DATABASE).query_db(query)
        if result:
            all_teams = []
            for team in result:
                all_teams.append(cls(team))
            return all_teams
        return None

    @classmethod
    def get_all_teams_by_user_id(cls, data):
        query = "SELECT * FROM teams WHERE teams.user_id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            all_teams = []
            for team in result:
                all_teams.append(cls(team))
            return all_teams
        return None

    @classmethod
    def get_one_team_by_user_id(cls, data):
        query = "SELECT * FROM teams JOIN users ON teams.id = users.team_id WHERE users.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return None

    @classmethod
    def get_one_team_by_team_name(cls, data):
        query = "SELECT * FROM teams WHERE teams.name = %(name)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return None

    @classmethod
    def save_team(cls, data):
        query = "INSERT INTO teams (name, user_id) VALUES (%(name)s, %(user_id)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def update_team(cls, data):
        query = "UPDATE teams SET name = %(name)s, user_id = %(user_id)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_team(cls, data):
        query = "DELETE FROM teams WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_edit_team_id(data):
        is_valid = True

        if not data['team_id']:
            flash('Please select your team.', 'error_edit_team_id')
            is_valid = False

        else:
            existing_team = Team.get_one_team_by_team_name(
                {'id': data['team_id']})
            if existing_team:
                flash('This team does not exist. Try a new name.', 'error_edit_team_id')
                is_valid = False

        return is_valid

    @staticmethod
    def validate_create_team_name(data):
        is_valid = True

        if len(data['name']) < 1:
            flash('Please enter the name of team.', 'error_create_team_name')
            is_valid = False

        else:
            existing_team = Team.get_one_team_by_team_name(
                {'name': data['name']})
            if existing_team:
                flash('This team name already exists. Try a new name.', 'error_create_team_name')
                is_valid = False

        return is_valid

    @staticmethod
    def validate_edit_team_name(data):
        is_valid = True

        if len(data['name']) < 1:
            flash('Please enter the name of team.', 'error_edit_team_name')
            is_valid = False

        else:
            existing_team = Team.get_one_team_by_team_name(
                {'name': data['name']})
            if existing_team:
                flash('This team name already exists. Try a new name.', 'error_edit_team_name')
                is_valid = False

        return is_valid