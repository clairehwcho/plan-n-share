from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import os
from dotenv import load_dotenv
load_dotenv(override=True)

DATABASE = os.environ.get("DB_NAME")


class Team:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

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
    def get_one_team_by_user_id(cls, data):
        query = "SELECT * FROM teams JOIN users ON teams.id = users.team_id WHERE users.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)

        if result:
            return cls(result[0])

        return None

    @classmethod
    def get_one_team_by_team_name(cls, data):
        query = "SELECT * FROM teams WHERE name = %(name)s"
        result = connectToMySQL(DATABASE).query_db(query, data)

        if result:
            return cls(result[0])

        return None

    @classmethod
    def create_team(cls, data):
        query = "INSERT INTO teams (name, user_id) VALUES (%(name)s, %(user_id)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    # @classmethod
    # def update_team(cls, data):
    #     query = "UPDATE teams SET name = %(name)s, user_id = %(user_id)s WHERE id = %(id)s;"
    #     result = connectToMySQL(DATABASE).query_db(query, data)
    #     return result

    # @classmethod
    # def delete_team(cls, data):
    #     query = "DELETE FROM teams WHERE id = %(id)s;"
    #     result = connectToMySQL(DATABASE).query_db(query, data)
    #     return result

    @staticmethod
    def validate_create_team(data):
        is_valid = True

        if len(data["name"]) < 1:
            flash("Please enter the name of team.", "error_create_team")
            is_valid = False

        else:
            existing_team = Team.get_one_team_by_team_name(
                {"name": data["name"]})

            if existing_team:
                flash("This team name already exists. Try a new name.", "error_create_team")
                is_valid = False

        return is_valid