from flask import render_template, redirect, session
from flask_app import app
from flask_app.models.model_task import Task
from flask_app.models.model_team import Team


@app.route('/')
def render_index():
    try:
        if 'user_id' in session:
            return redirect('/dashboard')

        return render_template("index.html")

    except:
        return render_template("error.html")


@app.route('/dashboard')
def render_dashboard():
    try:
        if 'user_id' not in session:
            return redirect('/')

        if session['team_id'] is None:
            return redirect('/teams')

        user_data = {
            "id": session['user_id'],
            "team_id": session['team_id']
        }

        all_user_tasks = Task.get_all_user_tasks(user_data)
        all_team_tasks = Task.get_all_team_tasks(user_data)
        current_team = Team.get_one_team_by_user_id(user_data)

        return render_template(
            'dashboard.html',
            all_user_tasks=all_user_tasks,
            all_team_tasks=all_team_tasks,
            current_team=current_team,
        )

    except:
        return render_template("error.html")


@app.errorhandler(404)
def handle_not_found(e):
    return render_template("error.html")
