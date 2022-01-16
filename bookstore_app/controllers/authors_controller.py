"""
This module implements services for authors, used to make database queries
"""
import sqlalchemy
from bookstore_app.forms.author_form import AuthorForm
from bookstore_app.service.authors_service import AuthorsService
from bookstore_app.service.dependency_error import DependencyError
from flask import flash, request


class AuthorsController:
    """
    This class implements services for authors, used to make database queries
    """
    authors_service = AuthorsService()

    @classmethod
    def get_authors(cls):
        """
        Fetches all authors from database
        :return: genres
        """
        authors, avg_rate = cls.authors_service.get_authors()
        return authors, avg_rate

    @classmethod
    def add_author(cls):
        """
        Add new author to database
        :return: form
        """
        form = AuthorForm()
        try:
            if form.name.data is None or form.name.data == "" or form.birth_date.data == "":
                flash("Fill in the data please!")
            elif form.validate_on_submit():
                cls.authors_service.add_author(form.name.data, form.birth_date.data)

                form.name.data = ""
                form.birth_date.data = ""

                flash("Author added successfully!")
        except sqlalchemy.exc.OperationalError:
            flash("This author already exists!")
        return form

    @classmethod
    def delete_author(cls, id):
        """
        Delete author by id, and fetches other authors from database
        :param id: author id
        :return: all authors in the database, except which we delete
        """
        try:
            cls.authors_service.delete_author(id)
            flash("Author deleted successfully!")
        except DependencyError:
            flash("Sorry, you can't delete this author, you have books by this author!")
        except:
            flash("Oops something went wrong.. try again")

        authors = cls.authors_service.get_authors()

        return authors

    @classmethod
    def update_author(cls, id):
        """
        Update author by id
        :param id: author id
        :return: form with fields for update, author for update
        """
        form = AuthorForm()
        author_to_update = cls.authors_service.get_author(id)
        if request.method == "POST":
            try:
                cls.authors_service.update_author(id, form.name.data, form.birth_date.data)
                flash("Author updated successfully!")
                return form, author_to_update

            except:
                flash("Error! Looks like there was a problem! Try again...")
                return form, author_to_update
        else:
            return form, author_to_update
