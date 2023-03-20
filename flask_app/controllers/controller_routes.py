from flask import render_template, redirect, session
from flask_app import app
from flask_app.models.model_task import Task
from flask_app.models.model_team import Team


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    if session['team_id'] is None:
        return redirect('/team')

    user_data = {
        "id": session['user_id'],
    }
    team_data = {
        "id": session['team_id']
    }
    all_user_tasks = Task.get_all_user_tasks_by_user_id(user_data)
    all_team_tasks = Task.get_all_team_tasks_by_team_id(team_data)
    all_teams = Team.get_all_teams()
    current_team = Team.get_one_team_by_user(user_data)
    return render_template(
        'dashboard.html',
        all_user_tasks=all_user_tasks,
        all_team_tasks=all_team_tasks,
        all_teams=all_teams,
        current_team=current_team
    )