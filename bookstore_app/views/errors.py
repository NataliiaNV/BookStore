"""
This module implements rendering custom error pages
"""

from flask import render_template
from app import app


@app.errorhandler(404)
def page_not_found(e):
    """
    method render 404 error page
    :return: 404 error page view
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    """
    method render 500 error page
     :return: 500 error page view
    """
    return render_template('500.html'), 500