import os
import psycopg2
from flask import Flask
from passlib.hash import sha256_crypt
from app.config import configuration

app = Flask(__name__)
config = configuration.get(os.environ.get("APP_ENV", "development"))
app.config.from_object(config)

DatabaseConnection = psycopg2.connect(
  database = config.DATABASE_NAME, 
  password = config.DATABASE_PASSWORD, 
  user = config.DATABASE_USER, 
  host = config.DATABASE_HOST, 
  port = 5432
  )

# create_db_tables()
# if os.getenv() === ''


# DatabaseConnection = psycopg2.connect(database ="testdb")

from app.routes.user_routes import UserUrl
UserUrl.get_user_routes(app)

from app.routes.incident_routes import IncidentUrl
IncidentUrl.get_incident_routes(app)

from app.routes.incident_routes import UpdateUrl
UpdateUrl.update_the_comment_routes(app)

from app.routes.incident_routes import UpdateStatus
UpdateStatus.update_status(app)
