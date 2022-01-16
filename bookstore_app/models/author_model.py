"""
This module implements instance of author in database
"""

from bookstore_app import db
from bookstore_app.models.book_model import Book


class Author(db.Model):
    """
    Author object stands for representation data in authors table
    :param id: id of author in db
    :param name: author's name
    :param birth_date: author's birth date
    :param book_id: book id
    """
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    birth_date = db.Column(db.DateTime)
    book_id = db.relationship("Book", backref="auth", foreign_keys=[Book.author_id])

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def __repr__(self):
        """
        Method gives representation of authors
        :return: string with author id, name, birth_date, book_id
        """
        return f"Author(id: {self.id}, name: {self.name}, birth_date: {self.birth_date}, book_id: {self.book_id})"
