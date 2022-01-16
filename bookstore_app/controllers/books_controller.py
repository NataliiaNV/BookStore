"""
This module implements services for books, used to make database queries
"""
import sqlalchemy
from bookstore_app.forms.book_form import BookForm
from bookstore_app.service.books_service import BooksService
from bookstore_app.service.genres_service import GenresService
from bookstore_app.service.authors_service import AuthorsService
from flask import flash, request
from datetime import datetime


class BooksController:
    """
    This class implements services for books, used to make database queries
    """
    books_service = BooksService()
    authors_service = AuthorsService()
    genres_service = GenresService()

    @classmethod
    def get_books(cls):
        """
        Fetches all books from database
        :return: books
        """
        books = cls.books_service.get_books_api()
        return books

    @classmethod
    def add_book(cls):
        """
        Add new book to database
        :return: form for posting new book's data
        """
        form = BookForm()
        form.genre_id.choices = [(row.id, row.name) for row in cls.genres_service.get_genres()]
        form.author_id.choices = [(row.id, row.name) for row in cls.authors_service.get_authors()[0]]
        try:
            if form.name.data is None or form.name.data == "":
                flash("Fill in the data please!")
            elif datetime.strptime(form.publish_date.data, "%Y-%m-%d") > datetime.today():
                flash("Please choose the correct date!")
            elif form.validate_on_submit():
                cls.books_service.add_book(form.name.data, form.author_id.data, form.genre_id.data,
                                           form.publish_date.data, form.description.data, form.price.data,
                                           form.rating.data)

                # clear form
                form.name.data = ""
                form.author_id.data = ""
                form.genre_id.data = ""
                form.publish_date.data = ""
                form.description.data = ""
                form.price.data = ""
                form.rating.data = ""

                flash("Book added successfuly!")
        except sqlalchemy.exc.IntegrityError:
            flash("Check please your data!")
        except sqlalchemy.exc.OperationalError:
            flash("Check formats please!")
        return form

    @classmethod
    def delete_book(cls, id):
        """
        Delete book by id, and fetches other books from database
        :param id: book id
        :return: all books in the database, except which we delete
        """
        try:
            cls.books_service.delete_book(id)
            flash("Book deleted successfully!")
        except:
            flash("Oops something went wrong.. try again")
        books = cls.books_service.get_books()
        return books

    @classmethod
    def update_book(cls, id):
        """
        Update book by id
        :param id: book id
        :return: form with fields for update, genre for update
        """
        form = BookForm()
        book_to_update = cls.books_service.get_book(id)

        form.genre_id.choices = [(row.id, row.name) for row in cls.genres_service.get_genres()]
        form.author_id.choices = [(row.id, row.name) for row in cls.authors_service.get_authors()[0]]

        genre_ind = [choice[0] for choice in form.genre_id.choices].index(book_to_update.genre_id)
        form.genre_id.choices.insert(0, form.genre_id.choices.pop(genre_ind))

        auth_ind = [choice[0] for choice in form.author_id.choices].index(book_to_update.author_id)
        form.author_id.choices.insert(0, form.author_id.choices.pop(auth_ind))

        if request.method == "POST":

            try:
                if datetime.strptime(form.publish_date.data, "%Y-%m-%d") > datetime.today():
                    flash("Please choose the correct date!")
                    return form, book_to_update
                else:
                    cls.books_service.update_book(id, form.name.data, form.author_id.data, form.genre_id.data,
                                                  form.publish_date.data, form.description.data, form.price.data,
                                                  form.rating.data)
                    flash("Book updated successfully!")
                    return form, book_to_update
            except:
                flash("Error! Looks like there was a problem! Try again...")
                return form, book_to_update
        else:
            return form, book_to_update
