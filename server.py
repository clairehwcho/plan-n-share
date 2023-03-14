from flask_app import app
# Remember to continually add controller files as you create them
from flask_app.controllers import controller_routes, controller_users, controller_tasks, controller_teams

# This needs to be at the bottom
if __name__ == "__main__":
    app.run(debug=True)