"""
This module implements services for author, used to make database queries
"""

from bookstore_app import db
from bookstore_app.models.author_model import Author
from bookstore_app.models.book_model import Book
from bookstore_app.service.genres_service import DependencyError


class AuthorsService:
    """
    This class implements services for authors, used to make database queries
    """

    @classmethod
    def __avg_rate(cls):
        """
        Calculate avg_rate rating for authors based on theirs books
        :return: avg_rate
        """
        avg_rate = db.session.query(Author.id, db.func.round(db.func.avg(Book.rating), 2)). \
            join(Author).group_by(Author.id).all()

        return avg_rate

    @classmethod
    def get_author(cls, id):
        """
        Fetches specific genre from database
        :param id: author id
        :return: author
        """
        author = Author.query.get_or_404(id)
        return author


    @classmethod
    def get_authors(cls):
        """
        Fetches all authors from database and paging it
        :return: list of all authors, dict(avg_rate)
        """
        avg_rate = cls.__avg_rate()
        our_authors = Author.query.order_by(Author.id).all()
        return our_authors, dict(avg_rate)


    @classmethod
    def add_author(cls, name, birth_date):
        """
        Add new author to database
        :param name: author name
        :param birth_date: author's birth date
        :return: None
        """

        new_auth = Author(name=name, birth_date=birth_date)
        db.session.add(new_auth)
        db.session.commit()
        return None


    @classmethod
    def delete_author(cls, id):
        """
        Delete author by id, and fetches other authors from database and paging it
        :param id: the id of the author we want to delete
        :return: all authors in the database, except which we delete, avg_rate rating for authors based on their books
        """
        author_to_delete = Author.query.get_or_404(id)

        if not db.session.query(db.session.query(Book).filter_by(author_id=id).exists()).scalar():
            db.session.delete(author_to_delete)
            db.session.commit()
        else:
            raise DependencyError
        return None


    @classmethod
    def update_author(cls, id, name, birth_date):
        """
        Update author by id
        :param id: author id
        :param name: author name
        :param birth_date: author birth date
        :return: None
        """

        author_to_update = Author.query.get_or_404(id)

        if name:
            author_to_update.name = name
        if birth_date:
            author_to_update.birth_date = birth_date
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise DependencyError

        return None





