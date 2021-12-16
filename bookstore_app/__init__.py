from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

import logging
from logging.config import dictConfig
from logconfig import LOGGING

from flask_marshmallow import Marshmallow

dictConfig(LOGGING)

# create a Flask instance
app = Flask(__name__)
app.logger = logging.getLogger('bookstore')
app.logger.info("BookStore started")


db = SQLAlchemy(app)

migrate = Migrate(app, db)

app.config.from_object(Config)

# ma = Marshmallow(app)

from bookstore_app.views import home, authors, genres, search, books

