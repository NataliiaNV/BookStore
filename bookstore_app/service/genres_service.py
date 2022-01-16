"""
This module implements services for genres, used to make database queries
"""


from bookstore_app.models.genre_model import Genre
from bookstore_app.models.book_model import Book
from bookstore_app import db


class GenresService:
    """
    This class implements services for genres, used to make database queries
    """
    @classmethod
    def get_genre(cls, id):
        """
        Fetches specific genre from database
        :param id: genre id
        :return: genres
        """
        genre = Genre.query.get_or_404(id)
        return genre

    @classmethod
    def get_genres(cls):
        """
        Fetches all genres from database
        :return: genres
        """
        genres = Genre.query.order_by(Genre.id).all()
        return genres

    @classmethod
    def add_genre(cls,  name, description):
        """
        Add new genre to database
        :param name: name of the genre
        :param description: description of the genre
        """
        new_genre = Genre(name=name, description=description)
        db.session.add(new_genre)
        db.session.commit()
        return None

    @classmethod
    def delete_genre(cls, id):
        """
        Delete genre by id, and fetches other genres from database
        :param id: genre id
        :return: None
        """
        genre_to_delete = Genre.query.get_or_404(id)

        if not db.session.query(db.session.query(Book).filter_by(genre_id=id).exists()).scalar():
            db.session.delete(genre_to_delete)
            db.session.commit()
        else:
            raise DependencyError

        return None


    @classmethod
    def update_genre(cls, id, name, description):
        """
        Update genre by id
        :param id: genre id
        :param name: genre name
        :param description: genre description
        :return: None
        """
        genre_to_update = Genre.query.get_or_404(id)

        if name:
            genre_to_update.name = name
        if description:
            genre_to_update.description = description
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise DependencyError

        return None


class DependencyError(Exception):
    """Raised when there are dependencies which prevent entity from being deleted"""
    pass
