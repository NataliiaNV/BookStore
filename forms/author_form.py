"""
This module implements instance of author web form
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AuthorForm(FlaskForm):
    """
    Custom FlaskForm object for author form.
    """
    name = StringField("Author name", validators=[DataRequired()])
    birth_date = StringField("Birth date", validators=[DataRequired()])
    submit = SubmitField("Submit")

