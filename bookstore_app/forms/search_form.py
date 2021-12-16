"""
This module implements instance of search web form
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")


class RangeSearchForm(FlaskForm):
    searched_1 = StringField("Searched", validators=[DataRequired()])
    searched_2 = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")