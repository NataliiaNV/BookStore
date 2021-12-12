"""
This module implements rendering home page
"""

from flask import render_template, flash
from bookstore_app import app

from bookstore_app.models.genre_model import Genre


@app.route('/')
@app.route('/home')
@app.route('/genres')
def index():
    """
    Returns rendered `home.html` template for url route `/` , `/home`
    :return: rendered `home.html` template
    """
    flash('Welcome to our website!')
    genres = Genre.query.order_by(Genre.id)
    return render_template('home.html', genres=genres)



