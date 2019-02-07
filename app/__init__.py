import psycopg2
from flask import Flask
from flask_bcrypt import  Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config["SECRET_KEY"] = "thisismysecretkey"

DatabaseConnection = psycopg2.connect(database ="jenny", password = "postgres", user ="postgres", host="localhost", port=5432)

from app.routes.user_routes import UserUrl
UserUrl.get_user_routes(app)

from app.routes.incident_routes import IncidentUrl
IncidentUrl.get_incident_routes(app)

from app.routes.incident_routes import UpdateUrl
UpdateUrl.update_the_comment_routes(app)

from app.routes.incident_routes import UpdateStatus
UpdateStatus.update_status(app)
