from flask import render_template, request, redirect, session
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
    user_data = {
        'id': session['user_id'],
    }
    team_data = {
        'id': session['team_id'],
        'category': 'Public'
    }
    all_tasks = Task.get_all_tasks_by_user(user_data)
    all_public_tasks = Task.get_all_public_tasks_by_team(team_data)
    current_team = Team.get_one_team_by_user(user_data)
    return render_template('dashboard.html', all_tasks = all_tasks, all_public_tasks = all_public_tasks, current_team = current_team)