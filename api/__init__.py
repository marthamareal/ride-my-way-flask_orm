import os
from flask import Flask, Blueprint, jsonify
from flask_restplus import Api
from flask_migrate import Migrate
from flask_script import Manager
from .utilities.base_validator import ValidationError

app_blue_print = Blueprint('app_blue_print', __name__, url_prefix='/api')

api = Api(app_blue_print)

def create_app(config_type):

    """ Craetes an instace of the application from Flask
        
        Returns:
            The created flask application
    """

    import api.views

    # create Flask instance
    app = Flask(__name__)

    # register blueprint instance to the app
    app.register_blueprint(app_blue_print)

    # set database according to the environment 
    app.config.from_object(config_type)

    from database import db
    # connect app to the db
    db.init_app(app)
    
    # initialize migration scripts
    Migrate(app, db)

    # initialize Manager for db migrations
    Manager(app)

    return app

@api.errorhandler(ValidationError)
@app_blue_print.app_errorhandler(ValidationError)
def handle_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
