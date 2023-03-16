from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.model_team import Team
from flask_app.models.model_user import User
from flask_app.models.model_task import Task

@app.route('/tasks/new')
def add_task():
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id': session['user_id'],
        'team_id': session['team_id']
    }
    current_team = Team.get_one_team_by_user(user_data)
    all_team_users = User.get_all_users_by_team_id(user_data)
    return render_template(
        "add-task.html",
        current_team=current_team,
        all_team_users=all_team_users
        )

@app.route('/tasks/create', methods=['POST'])
def save_task():
    if not Task.validate_tasks(request.form):
        return redirect('/tasks/new')
    task_data = {
        **request.form,
        "user_id": session['user_id'],
    }
    Task.save(task_data)
    return redirect('/dashboard')


@app.route('/tasks/<int:id>')
def show_one_task(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    current_task = Task.get_one_with_users(data)
    return render_template('task_show.html', current_task = current_task)

@app.route('/tasks/<int:id>/edit')
def show_edit_task(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    current_task = Task.get_one_with_users(data)
    return render_template("task_edit.html", current_task = current_task)

@app.route('/tasks/<int:id>/update', methods=['POST'])
def update_task(id):
    if not Task.validate_tasks(request.form):
        return redirect(f'/tasks/edit/{id}')
    task_data = {
        **request.form,
        "id" : id,
        "user_id": session['user_id']
    }
    Task.update_one(task_data)
    return redirect('/dashboard')

@app.route('/tasks/<int:id>/delete')
def delete_task(id):
    data = {
        "id" : id,
    }
    Task.delete_one(data)
    return redirect('/dashboard')