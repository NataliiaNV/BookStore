from flask import Flask, render_template, flash, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



# create a Flask instance
app = Flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Qazxsw101100!@localhost/bookstore'
app.config['SECRET_KEY'] = 'my secret key'

