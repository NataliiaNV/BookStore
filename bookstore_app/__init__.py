from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_marshmallow import Marshmallow

import logging
from logging.config import dictConfig
from logconfig import LOGGING


dictConfig(LOGGING)


app = Flask(__name__)
app.logger = logging.getLogger('bookstore')
app.logger.info("BookStore started")

db = SQLAlchemy(app)
ma = Marshmallow(app)

migrate = Migrate(app, db)

app.config.from_object(Config)


from bookstore_app.views import home, authors, genres, search, books
from bookstore_app.rest.rest import api

app.register_blueprint(api, url_prefix='/api')
