from flask_app import app
from flask_app.controllers import controller_routes, controller_users, controller_tasks, controller_teams

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')