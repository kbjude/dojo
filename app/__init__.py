import os
from flask import Flask
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
