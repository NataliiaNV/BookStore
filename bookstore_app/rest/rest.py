"""
Module is made for handling with REST-API requests.
"""

import sqlalchemy
from flask import Blueprint
from flask import request
from datetime import datetime

from bookstore_app.service.authors_service import AuthorsService
from bookstore_app.service.books_service import BooksService
from bookstore_app.service.genres_service import GenresService, DependencyError

from bookstore_app.rest.schemas import AuthorSchema, BookSchema, GenreSchema


api = Blueprint('api', __name__)

authors_service = AuthorsService()
books_service = BooksService()
genres_service = GenresService()

authors_schema = AuthorSchema(many=True)
books_schema = BookSchema(many=True)
genres_schema = GenreSchema(many=True)


@api.route('/genres', methods=['GET'])
def get_genres():
    """
    Fetches all genres.
    :return: dict
    """
    genres = genres_service.get_genres()
    return genres_schema.jsonify(genres).data


@api.route('/genres', methods=['POST'])
def add_genre():
    """
    Add new genre to database. Return new genre in json format.
    :return: dict
    """
    name = request.json.get('name')
    description = request.json.get('description')

    if not name or not description:
        return {'error': {'message': 'Missed some data', 'status': 400}}, 400
    try:
        genres_service.add_genre(name, description)
        return {'OK': {'message': 'New genre added', 'status': 200}}
    except sqlalchemy.exc.IntegrityError:
        return {'error': {'message': 'This genre already exists!', 'status': 400}}, 400


@api.route('/genres/<int:id>', methods=['DELETE'])
def delete_genre(id):
    """
    Delete genre with given id from database
    :param id: id of genre to delete
    :return: dict
    """
    try:
        genres_service.delete_genre(id)
    except DependencyError:
        return {'error': {'message': 'You can\'t delete this genre, you have books of this genre!', 'status': 400}}, 400
    except:
        return {'error': {'message': 'There was a problem with deleting genre', 'status': 500}}, 500

    return {'OK': {'message': 'Genre deleted', 'status': 200}}


@api.route('/genres/<int:id>', methods=['PATCH'])
def update_genre(id):
    """
    Update genre with given id
    :param id: id of genre to update
    :return: dict
    """
    try:
        name = request.json.get('name')
        description = request.json.get('description')
        genres_service.update_genre(id, name, description)
    except:
        return {'error': {'message': 'There was a problem with updating genre', 'status': 500}}, 500

    return {'OK': {'message': 'Genre updated', 'status': 200}}


@api.route('/authors', methods=['GET'])
def get_authors():
    """
    Fetches all authors.
    :return: dict
    """
    authors, avg_rate = authors_service.get_authors()
    return authors_schema.jsonify(authors).data


@api.route('/authors', methods=['POST'])
def add_author():
    """
    Add new author to database. Return new author in json format.
    :return: dict
    """
    name = request.json.get('name')
    birth_date = request.json.get('birth_date')

    if not name or not birth_date:
        return {'error': {'message': 'Missed some data', 'status': 400}}, 400
    try:
        authors_service.add_author(name, birth_date)
        return {'OK': {'message': 'New author added', 'status': 200}}
    except (sqlalchemy.exc.OperationalError, sqlalchemy.exc.IntegrityError):
        return {'error': {'message': 'Check you data!', 'status': 400}}, 400


@api.route('/authors/<int:id>', methods=['DELETE'])
def delete_author(id):
    """
    Delete author with given id from database
    :param id: id of author to delete
    :return: dict
    """
    try:
        authors_service.delete_author(id)
    except DependencyError:
        return {'error': {'message': 'You can\'t delete this author, you have books by this author!',
                          'status': 400}}, 400
    except:
        return {'error': {'message': 'There was a problem with deleting author', 'status': 500}}, 500

    return {'OK': {'message': 'Author deleted', 'status': 200}}


@api.route('/authors/<int:id>', methods=['PATCH'])
def update_author(id):
    """
    Update author with given id
    :param id: id of author to update
    :return: dict
    """
    try:
        name = request.json.get('name')
        birth_date = request.json.get('birth_date')
        authors_service.update_author(id, name, birth_date)
    except:
        return {'error': {'message': 'There was a problem with updating author', 'status': 500}}, 500

    return {'OK': {'message': 'Author updated', 'status': 200}}


@api.route('/books', methods=['GET'])
def get_books():
    """
    Fetches all books.
    :return: dict
    """
    books = books_service.get_books_api()
    return books_schema.jsonify(books).data


@api.route('/books', methods=['POST'])
def add_book():
    """
    Add new book to database. Return new book in json format.
    :return: dict
    """
    name = request.json.get('name')
    author_id = request.json.get('author_id')
    genre_id = request.json.get('genre_id')
    publish_date = request.json.get('publish_date')
    description = request.json.get('description')
    price = request.json.get('price')
    rating = request.json.get('rating')

    if not name or not author_id or not genre_id or not price or not publish_date or not rating:
        return {'error': {'message': 'Missed some data', 'status': 400}}, 400
    elif datetime.strptime(publish_date, "%Y-%m-%d") > datetime.today():
        return {'error': {'message': 'Check publish_date', 'status': 400}}, 400
    try:
        books_service.add_book(name, author_id, genre_id, publish_date, description, price, rating)
        return {'OK': {'message': 'New book added', 'status': 200}}
    except sqlalchemy.exc.IntegrityError:
        return {'error': {'message': 'Check your data!', 'status': 400}}, 400
    except:
        return {'error': {'message': 'There was a problem, try again...', 'status': 500}}, 500


@api.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    """
    Delete book with given id from database
    :param id: id of book to delete
    :return: dict
    """
    try:
        books_service.delete_book(id)
    except:
        return {'error': {'message': 'There was a problem with deleting book', 'status': 500}}, 500
    return {'OK': {'message': 'Book deleted', 'status': 200}}


@api.route('/books/<int:id>', methods=['PATCH'])
def update_book(id):
    """
    Update book with given id
    :param id: id of book to update
    :return: dict
    """
    try:
        name = request.json.get('name')
        author_id = request.json.get('author_id')
        genre_id = request.json.get('genre_id')
        publish_date = request.json.get('publish_date')
        description = request.json.get('description')
        price = request.json.get('price')
        rating = request.json.get('rating')

        books_service.update_book(id, name, author_id, genre_id, publish_date, description, price, rating)
    except:
        return {'error': {'message': 'There was a problem with updating book', 'status': 500}}, 500

    return {'OK': {'message': 'Book updated', 'status': 200}}
