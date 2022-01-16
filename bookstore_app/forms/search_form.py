"""
This module implements instance of search web form
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    """
    Custom FlaskForm object for search form.
    """
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")


class SearchDateForm(FlaskForm):
    """
    Custom FlaskForm object for search form.
    """
    date_searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")


class RangeSearchForm(FlaskForm):
    """
    Custom FlaskForm object for search form by dates range.
    """
    searched_1 = StringField("Searched", validators=[DataRequired()])
    searched_2 = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")
