'''
Author: David Crook
Copyright: Microsoft Corporation 2018
'''
from flask_mongoengine import MongoEngine
from flask_security import UserMixin, RoleMixin, MongoEngineUserDatastore

db = MongoEngine()

class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

class User(db.Document, UserMixin):
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    first_name = db.StringField(max_length=255)
    last_name = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])
    current_login_at = db.DateTimeField()
    current_login_ip = db.StringField()
    last_login_at = db.DateTimeField()
    last_login_ip = db.StringField()
    login_count = db.IntField()

    @staticmethod
    def get_all():
        try:
            users = User.objects
            return users
        except Exception as ex:
            print('User.get_all() exception: {}'.format(ex))
            return None

user_datastore = MongoEngineUserDatastore(db, User, Role)
