"""
This module implements instance of book genre in database
"""

from bookstore_app import db
from bookstore_app.models.book_model import Book


class Genre(db.Model):
    """
        Genre object stands for representation data in genres table.
        :param id: id of book genre in db
        :param name: genre name
        :param description: genre description
    """

    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(1200))
    book_id = db.relationship('Book', backref='genr', foreign_keys=[Book.genre_id])

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        """
        method gives representation of genres
        :return: string with genre id, name, description
        """
        return f"Genre(id: {self.id}, name: {self.name}, description: {self.description})"


