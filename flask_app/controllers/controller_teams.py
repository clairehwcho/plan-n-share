from flask import render_template, request, redirect, session
from flask_app import app, bcrypt
from flask_app.models.model_team import Team
from flask_app.models.model_user import User

@app.route('/teams')
def manage_teams():
    if 'user_id' not in session:
        return redirect('/')

    if session['team_id']:
        return redirect('/dashboard')

    all_teams = Team.get_all_teams()
    return render_template('manage_teams.html', all_teams = all_teams)


@app.route('/teams/create', methods=['POST'])
def create_team():
    # validations
    if not Team.validate_create_team(request.form):
        return redirect('/teams')
    team_id = Team.save(request.form)
    session['team_id']=team_id
    user_data = {
        'team_id': session['team_id'],
        'id' : session['user_id']
    }
    User.update(user_data)
    return redirect('/dashboard')

@app.route('/team/join', methods=['POST'])
def join_team():
    # validations
    if not Team.validate_join_team(request.form):
        return redirect('/teams')
    current_team = Team.get_one_id_by_name(request.form)
    session['team_id'] = current_team.id
    user_data = {
        'team_id': session['team_id'],
        'id' : session['user_id']
    }
    User.update(user_data)
    return redirect('/dashboard')