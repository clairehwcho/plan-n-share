from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.model_team import Team
from flask_app.models.model_user import User
from flask_app.models.model_task import Task


@app.route('/tasks/new')
def render_add_task():
    # try:
        if 'user_id' not in session:
            return redirect('/')

        if session['team_id'] is None:
            return redirect('/teams')

        user_data = {
            'id': session['user_id'],
            'team_id': session['team_id']
        }

        current_team = Team.get_one_team_by_user_id(user_data)
        all_team_users = User.get_all_users_by_team_id(user_data)

        return render_template(
            "add_task.html",
            current_team=current_team,
            all_team_users=all_team_users
        )
    # except:
    #     return render_template("error.html")


@app.route('/tasks/new/create', methods=['POST'])
def create_task():
    try:
        if 'user_id' not in session:
            return redirect('/')

        if session['team_id'] is None:
            return redirect('/teams')

        if not Task.validate_task(request.form):
            return redirect('/tasks/new')

        task_data = {
            **request.form,
            "user_id": session['user_id'],
            "team_id": session['team_id']
        }

        try:
            Task.save_task(task_data)
        except:
            return redirect('tasks/new')

        return redirect('/dashboard')
    except:
        return render_template("error.html")

@app.route('/tasks/<int:id>/edit')
def render_edit_task(id):
    try:
        if 'user_id' not in session:
            return redirect('/')

        if session['team_id'] is None:
            return redirect('/teams')

        task_data = {
            "id": id
        }
        user_data = {
            'id': session['user_id'],
            'team_id': session['team_id']
        }

        task = Task.get_one_task_by_task_id(task_data)
        current_team = Team.get_one_team_by_user_id(user_data)
        all_team_users = User.get_all_users_by_team_id(user_data)

        return render_template(
            "edit_task.html",
            task=task,
            current_team=current_team,
            all_team_users=all_team_users
        )
    except:
        return render_template("error.html")


@app.route('/tasks/<int:id>/update', methods=['POST'])
def update_task(id):
    try:
        if 'user_id' not in session:
            return redirect('/')

        if session['team_id'] is None:
            return redirect('/teams')

        if not Task.validate_task(request.form):
            return redirect(f'/tasks/{id}/edit')

        task_data = {
            **request.form,
            "id": id
        }

        try:
            Task.update_task(task_data)
        except:
            return redirect(f'/tasks/{id}/edit')

        return redirect('/dashboard')
    except:
        return render_template("error.html")

@app.route('/tasks/<int:id>/delete')
def delete_task(id):
    try:
        if 'user_id' not in session:
            return redirect('/')

        if session['team_id'] is None:
            return redirect('/teams')

        task_data = {
            "id": id,
        }

        try:
            Task.delete_task(task_data)
            return redirect('/dashboard')
        except:
            return redirect('/dashboard')
    except:
        return render_template("error.html")