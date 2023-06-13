from flask import render_template, request, redirect, session, flash
from flask_app import app, bcrypt
from flask_app.models.model_user import User
from flask_app.models.model_team import Team


@app.route('/login', methods=['POST'])
def login():
    try:
        if not User.validate_login(request.form):
            return redirect('/')

        current_user = User.get_one_user_by_email(request.form)
        session['user_id'] = current_user.id
        session['first_name'] = current_user.first_name
        session['email'] = current_user.email
        session['team_id'] = current_user.team_id
        return redirect('/dashboard')
    except:
        return render_template("error.html")

@app.route('/logout')
def logout():
    try:
        session.clear()
        return redirect('/')
    except:
        return render_template("error.html")

@app.route('/register')
def render_register():
    try:
        return render_template('register.html')
    except:
        return render_template("error.html")

@app.route('/user/create', methods=['POST'])
def create_user():
    try:
        if not User.validate_register(request.form):
            return redirect('/register')

        hash_pw = bcrypt.generate_password_hash(request.form['password'])
        user_data = {
            **request.form,
            "password": hash_pw,
            "team_id": None
        }

        try:
            user_id = User.save(user_data)

            session['user_id'] = user_id
            session['first_name'] = user_data['first_name']
            session['email'] = user_data['email']
            session['team_id'] = user_data['team_id']
            return redirect('/dashboard')
        except:
            return redirect('/register')
    except:
        return render_template("error.html")

@app.route('/users/<int:id>/teams/default/update', methods=['POST'])
def update_team_id(id):
    try:
        if 'user_id' not in session:
            return redirect('/')

        if not Team.validate_edit_team_id(request.form):
            return redirect('/teams')

        user_data = {
            **request.form,
            "id": id
        }

        try:
            User.update(user_data)
            session['team_id'] = request.form['team_id']
            flash('Your default team has been successfully switched.',
                'info_edit_team_id_success')
        except:
            flash('Something went wrong. Try again.', 'error_edit_team_id')
        return redirect('/teams')
    except:
        return render_template("error.html")