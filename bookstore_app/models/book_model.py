"""
This module implements instance of book in database
"""

from bookstore_app import db


class Book(db.Model):
    """
    Book object stands for representation data in books table
    id: id of book in db
    name: book name
    author_id: author id
    genre_id: genre id
    description: book description
    price: book price
    rating: book rating
    """
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    publish_date = db.Column(db.DateTime)
    description = db.Column(db.String(1200))
    price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float)

    def __init__(self, name, author_id, genre_id, publish_date,  description, price, rating):
        self.name = name
        self.author_id = author_id
        self.genre_id = genre_id
        self.publish_date = publish_date
        self.description = description
        self.price = price
        self.rating = rating


    def __repr__(self):
        """
        Method gives representation of books
        :return: string with book id, name,author_id,genre_id, publish_date, description, price, rating
        """
        return f"Book(id: {self.id}, name: {self.name}, author_id: {self.author_id}, genre_id: {self.genre_id}," \
               f" publish_date: {self.publish_date}, description: {self.description}, price: {self.price}, rating: {self.rating})"
