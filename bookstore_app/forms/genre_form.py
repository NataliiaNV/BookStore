"""
This module implements instance of genre web form
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class GenreForm(FlaskForm):
    """
    Custom FlaskForm object for genre form.
    """
    name = StringField("Genre name", validators=[DataRequired()])
    description = StringField("Genre description", validators=[DataRequired()])
    submit = SubmitField("Add new genre")

