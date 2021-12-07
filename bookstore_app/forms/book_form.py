"""
This module implements instance of book web form
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    """
    Custom FlaskForm object for book form.
    """
    name = StringField("Book name", validators=[DataRequired()])
    author_id = StringField("Author id", validators=[DataRequired()])
    genre_id = StringField("Genre id", validators=[DataRequired()])
    publish_date = StringField("Publish date", validators=[DataRequired()])
    description = StringField("Book description", validators=[DataRequired()])
    price = StringField("Book price", validators=[DataRequired()])
    rating = StringField("Book rating", validators=[DataRequired()])
    submit = SubmitField("Add new author")


