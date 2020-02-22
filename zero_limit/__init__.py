from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from zero_limit.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from zero_limit import routes