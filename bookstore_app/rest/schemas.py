from bookstore_app import ma
from flask_marshmallow.fields import fields


class GenreSchema(ma.Schema):
    """
    GenreSchema class was made for serializing and deserializing class Genre
    :param id: id of book genre in db
    :param name: genre name
    :param description: genre description
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
    description = fields.Str()


class AuthorSchema(ma.Schema):
    """
    AuthorSchema class was made for serializing and deserializing class Author
    :param id: id of author in db
    :param name: author's name
    :param birth_date: author's birth date
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
    birth_date = fields.Date()


class BookSchema(ma.Schema):
    """
    BookSchema class was made for serializing and deserializing class Book
    :param id: id of book in db
    :param name: book name
    :param author_id: author id
    :param genre_id: genre id
    :param description: book description
    :param price: book price
    :param rating: book rating
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
    author_id = fields.Int()
    genre_id = fields.Int()
    description = fields.Str()
    price = fields.Float()
    publish_date = fields.Date()
    rating = fields.Float()
