from flask import render_template, request, redirect, session
from flask_app import app, bcrypt
from flask_app.models.model_user import User
from flask_app.models.model_team import Team


@app.route('/login', methods=['POST'])
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    current_user = User.get_one_user_by_email(request.form)
    session['user_id'] = current_user.id
    session['first_name'] = current_user.first_name
    session['email'] = current_user.email
    session['team_id'] = current_user.team_id
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/register')
def register():
    all_teams = Team.get_all_teams()
    return render_template('register.html', all_teams=all_teams)


@app.route('/user/create', methods=['POST'])
def create_user():
    if not User.validate_register(request.form):
        return redirect('/register')

    hash_pw = bcrypt.generate_password_hash(request.form['password'])
    user_data = {
        **request.form,
        'password': hash_pw,
    }

    user_id = User.save(user_data)

    session['user_id'] = user_id
    session['first_name'] = user_data['first_name']
    session['email'] = user_data['email']
    session['team_id'] = user_data['team_id']
    return redirect('/dashboard')
