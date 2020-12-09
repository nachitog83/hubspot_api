from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_cors import CORS
import os
import logging

logger = logging.getLogger('app')

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    
    app.config['PROPAGATE_EXCEPTIONS'] = False
    app.config['MONGODB_SETTINGS'] = {
    'host': os.environ['MONGODB_HOST'],
    'username': os.environ['MONGODB_USERNAME'],
    'password': os.environ['MONGODB_PASSWORD'],
    'db': 'webapp'
    }
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object('config')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():

        # Include our Routes
        from app.resources.routes import initialize_routes
        from app.resources.errors import errors
        from app.database.db import initialize_db

        # Initialize plugins
        api = Api(app, errors=errors)
        bcrypt = Bcrypt(app)
        jwt = JWTManager(app)
        ma = Marshmallow(app)


        # Imports

        # Initialize db
        initialize_db(app)
        initialize_routes(api)

        return app