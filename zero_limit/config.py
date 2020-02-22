import os

class Config(object):
    SECRET_KEY = os.environ.get('FLASK_KEY') or 'key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'