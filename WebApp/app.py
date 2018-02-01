'''
Author: David Crook
Copyright: Microsoft Corporation 2018
'''
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_security import Security

from forms.register_form import ExtendedRegisterForm
from extensions import csrf, toolbar

def create_app():
    app = Flask(__name__)

    # Config Stuff
    app.config.from_pyfile('config.py')

    # Register BluePrints
    from views import baseviews
    app.register_blueprint(baseviews)

    register_extensions(app)

    return app


def register_extensions(app):
    #from data.mongo.user import db, user_datastore

    db.init_app(app)

    csrf.init_app(app)    
    #security = Security(app, user_datastore, register_form=ExtendedRegisterForm)
