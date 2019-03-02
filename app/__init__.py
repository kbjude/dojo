import os
from flask import Flask
<<<<<<< HEAD
# from passlib.handlers.sha2_crypt import sha512_crypt
from app.config import configuration

app = Flask(__name__)
config = configuration.get(os.environ.get("APP_ENV", "development"))
app.config.from_object(config)

DatabaseConnection = psycopg2.connect(
    database=config.DATABASE_NAME,
    password=config.DATABASE_PASSWORD,
    user=config.DATABASE_USER,
    host=config.DATABASE_HOST,
    port=config.DATABASE_PORT
    )

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


from app.routes.user_routes import UserUrl
UserUrl.get_user_routes(app)

from app.routes.incident_routes import IncidentUrl
IncidentUrl.get_incident_routes(app)

from app.routes.incident_routes import UpdateUrl
UpdateUrl.update_the_comment_routes(app)

from app.routes.incident_routes import UpdateStatus
UpdateStatus.update_status(app)
=======
from logging.config import dictConfig

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


#index route
@app.route('/')
def index():
    """ index route """
    return "Welcome. This is a remix by the dojos.", 200


from app.routes import user_routes, incident_routes
>>>>>>> PatrickMugayaJoel-ch-refactor-to-run-164327460
