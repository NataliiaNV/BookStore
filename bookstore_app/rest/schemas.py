from bookstore_app import ma
from flask_marshmallow.fields import fields


class GenreSchema(ma.Schema):
    """
    GenreSchema class was made for serializing and deserializing class Genre
    id: id of book genre in db
    name: genre name
    description: genre description
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
    description = fields.Str()


class AuthorSchema(ma.Schema):
    """
    AuthorSchema class was made for serializing and deserializing class Author
    id: id of author in db
    name: author's name
    birth_date: author's birth date
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
    birth_date = fields.Date()


class BookSchema(ma.Schema):
    """
    BookSchema class was made for serializing and deserializing class Book
    id: id of book in db
    name: book name
    author_id: author id
    genre_id: genre id
    description: book description
    price: book price
    rating: book rating
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()
    author_id = fields.Int()
    genre_id = fields.Int()
    description = fields.Str()
    price = fields.Float()
    publish_date = fields.Date()
    rating = fields.Float()
