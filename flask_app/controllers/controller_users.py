from flask import render_template, request, redirect, session, flash
from flask_app import app, bcrypt
from flask_app.models.model_user import User
from flask_app.models.model_team import Team


@app.route('/signin', methods=['POST'])
def signin():
    try:
        if not User.validate_signin(request.form):
            return redirect('/')

        current_user = User.get_one_user_by_email(request.form)
        session['user_id'] = current_user.id
        session['first_name'] = current_user.first_name
        session['email'] = current_user.email
        session['team_id'] = current_user.team_id
        return redirect('/dashboard')

    except:
        return render_template("error.html")


@app.route('/signout')
def signout():
    try:
        session.clear()
        return redirect('/')

    except:
        return render_template("error.html")


@app.route('/register')
def render_register():
    try:
        if 'user_id' in session:
            return redirect('/dashboard')

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
            user_id = User.create_user(user_data)

            session['user_id'] = user_id
            session['first_name'] = user_data['first_name']
            session['email'] = user_data['email']
            session['team_id'] = user_data['team_id']
            return redirect('/dashboard')

        except:
            return redirect('/register')

    except:
        return render_template("error.html")


@app.route('/users/<int:id>/team/update', methods=['POST'])
def update_team_id(id):
    try:
        if 'user_id' not in session:
            return redirect('/')

        user_data = {
            **request.form,
            "id": id
        }

        try:
            User.update_user(user_data)
            session['team_id'] = request.form['team_id']
            flash('Your team has been successfully changed.',
                  'info_edit_team_id_success')
        except:
            flash('Something went wrong. Try again.', 'error_edit_team_id')
        return redirect('/teams')

    except:
        return render_template("error.html")
