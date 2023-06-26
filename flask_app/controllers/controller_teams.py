from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.model_team import Team
from flask_app.models.model_user import User


@app.route('/teams')
def render_manage_teams():
    # try:
        if 'user_id' not in session:
            return redirect('/')

        user_data = {
            'id': session['user_id'],
            'team_id': session['team_id']
        }

        current_team = Team.get_one_team_by_user_id(user_data)
        all_joined_teams = Team.get_all_teams_joined_by_user_id(user_data)
        all_unjoined_teams = Team.get_all_teams_unjoined_by_user_id(user_data)
        all_created_teams = Team.get_all_teams_created_by_user_id(user_data)
        all_teams = Team.get_all_teams()

        print (all_joined_teams)

        return render_template(
            'manage_teams.html',
            current_team=current_team,
            all_joined_teams=all_joined_teams,
            all_unjoined_teams=all_unjoined_teams,
            all_created_teams=all_created_teams,
            all_teams=all_teams
        )
    # except:
    #     return render_template("error.html")


@app.route('/teams/create', methods=['POST'])
def create_team():
    try:
        if 'user_id' not in session:
            return redirect('/')

        if not Team.validate_create_team_name(request.form):
            return redirect('/teams')

        team_data = {
            **request.form,
            "user_id": session['user_id']
        }

        try:
            Team.save_team(team_data)
            flash('A new team has been successfully created.', 'info_create_team_name_success')
            return redirect('/teams')
        except:
            flash('Something went wrong. Try again.', 'error_create_team_name')
    except:
        return render_template("error.html")


@app.route('/teams/<int:id>/update', methods=['POST'])
def update_team(id):
    try:
        if 'user_id' not in session:
            return redirect('/')

        if not Team.validate_edit_team_name(request.form):
            return redirect('/teams')

        team_data = {
            **request.form,
            "id": id,
            "user_id": session['user_id']
        }

        try:
            Team.update_team(team_data)
            return redirect('/teams')
        except:
            return redirect('/teams')
    except:
        return render_template("error.html")


@app.route('/teams/<int:id>/delete')
def delete_team(id):
    try:
        if 'user_id' not in session:
            return redirect('/')

        team_data = {
            "id": id,
        }

        try:
            Team.delete_team(team_data)
            return redirect('/teams')
        except:
            return redirect('/teams')
    except:
        return render_template("error.html")
