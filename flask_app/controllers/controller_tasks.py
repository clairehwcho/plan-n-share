from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.model_team import Team
from flask_app.models.model_user import User
from flask_app.models.model_task import Task


@app.route('/tasks/new')
def show_add_task_form():
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id': session['user_id'],
        'team_id': session['team_id']
    }
    current_team = Team.get_one_team_by_user(user_data)
    all_team_users = User.get_all_users_by_team_id(user_data)
    return render_template(
        "add_task.html",
        current_team=current_team,
        all_team_users=all_team_users
    )


@app.route('/tasks/new/create', methods=['POST'])
def save_new_task():
    if 'user_id' not in session:
        return redirect('/')
    if not Task.validate_task(request.form):
        return redirect('/tasks/new')
    task_data = {
        **request.form,
        "user_id": session['user_id'],
    }
    Task.save(task_data)
    return redirect('/dashboard')


@app.route('/tasks/<int:id>/edit')
def show_edit_task_form(id):
    if 'user_id' not in session:
        return redirect('/')
    task_data = {
        "id": id
    }
    user_data = {
        'id': session['user_id'],
        'team_id': session['team_id']
    }
    task = Task.get_one_task_by_task_id(task_data)
    current_team = Team.get_one_team_by_user(user_data)
    all_team_users = User.get_all_users_by_team_id(user_data)
    return render_template(
        "edit_task.html",
        task=task,
        current_team=current_team,
        all_team_users=all_team_users
    )


@app.route('/tasks/<int:id>/update', methods=['POST'])
def update_task(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Task.validate_task(request.form):
        return redirect(f'/tasks/{id}/edit')
    task_data = {
        **request.form,
        "id": id,
        "user_id": session['user_id']
    }
    Task.update(task_data)
    return redirect('/dashboard')


@app.route('/tasks/<int:id>/delete')
def delete_task(id):
    if 'user_id' not in session:
        return redirect('/')
    task_data = {
        "id": id,
    }
    Task.delete(task_data)
    return redirect('/dashboard')
