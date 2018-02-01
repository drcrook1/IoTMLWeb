'''
Author: David Crook
Copyright: Microsoft Corporation 2018
'''
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_security import Security
from flask_debugtoolbar import DebugToolbarExtension
from data.mongo.user import db, user_datastore

def create_app():
    app = Flask(__name__)

    # Config Stuff
    app.config.from_pyfile('config.py')

    # Register BluePrints
    from views.baseviews import baseviews
    app.register_blueprint(baseviews)

    from apis.sampleapi import testapi
    app.register_blueprint(testapi)

    register_extensions(app)

    return app

def register_extensions(app):
    toolbar = DebugToolbarExtension()
    #db.init_app(app)
    #security = Security(app, user_datastore, register_form=ExtendedRegisterForm)
