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
  port = config.DATABASE_PORT
  )

# DatabaseConnection = psycopg2.connect(os.environ.get('URI'))
DatabaseConnection.autocommit = True
cursor = DatabaseConnection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (user_id SERIAL PRIMARY KEY  NOT NULL,
                username VARCHAR(225) NOT NULL,
                password VARCHAR(225) NOT NULL,
                email VARCHAR(225) NOT NULL,
                phone_number VARCHAR(225) NOT NULL,
                is_admin VARCHAR(225) NOT NULL);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS incident
                (incident_id SERIAL PRIMARY KEY,
                incident_type VARCHAR(225) NOT NULL,
                title VARCHAR(225) NOT NULL,
                created_by INTEGER NOT NULL,
                location VARCHAR(225) NOT NULL,
                status  VARCHAR(225) DEFAULT 'draft',
                comment VARCHAR(225),
                created_on TIMESTAMP DEFAULT Now(),
                FOREIGN KEY (created_by)
                  REFERENCES users (user_id)
                  ON UPDATE CASCADE ON DELETE CASCADE);
                ''')


# DatabaseConnection = psycopg2.connect(database ="testdb")

from app.routes.user_routes import UserUrl
UserUrl.get_user_routes(app)

from app.routes.incident_routes import IncidentUrl
IncidentUrl.get_incident_routes(app)

from app.routes.incident_routes import UpdateUrl
UpdateUrl.update_the_comment_routes(app)

from app.routes.incident_routes import UpdateStatus
UpdateStatus.update_status(app)
