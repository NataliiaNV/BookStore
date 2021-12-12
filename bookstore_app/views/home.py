"""
This module implements rendering home page
"""

from flask import render_template, flash
from bookstore_app import app

@app.route('/')
@app.route('/home')
def index():
    """
    Returns rendered `home.html` template for url route `/` , `/home`
    :return: rendered `home.html` template
    """
    flash('Welcome to our website!')
    return render_template('home.html')



