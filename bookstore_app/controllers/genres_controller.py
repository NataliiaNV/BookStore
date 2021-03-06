"""
This module handles forms based on the data from genres service
"""
import sqlalchemy
from bookstore_app.forms.genre_form import GenreForm
from bookstore_app.service.genres_service import GenresService
from bookstore_app.service.dependency_error import DependencyError
from flask import flash, request


class GenresController:
    """
    This class handles forms based on the data from genres service
    """
    genres_service = GenresService()

    @classmethod
    def get_genres(cls):
        """
        Fetches all genres from database
        :return: genres
        """
        genres = cls.genres_service.get_genres()
        return genres

    @classmethod
    def add_genre(cls):
        """
        Add new genre to database
        :return: form
        """
        form = GenreForm()
        try:
            if form.name.data is None or form.name.data == "":
                flash("Fill in the data please!")
            elif form.validate_on_submit():
                cls.genres_service.add_genre(form.name.data, form.description.data)

                form.name.data = ""
                form.description.data = ""

                flash("Genre added successfully!")
        except sqlalchemy.exc.IntegrityError:

            flash("This genre already exists!")

        return form

    @classmethod
    def delete_genre(cls, id):
        """
        Delete genre by id, and fetches other genres from database
        :param id: genre id
        :return: all genres in the database, except which we delete
        """
        try:
            cls.genres_service.delete_genre(id)
            flash("Genre deleted successfully!")
        except DependencyError:
            flash("Sorry, you can't delete this genre, you have books of this genre!")
        except:
            flash("Oops something went wrong.. try again")

        genres = cls.genres_service.get_genres()

        return genres

    @classmethod
    def update_genre(cls, id):
        """
        Update genre by id
        :param id: genre id
        :return: form with fields for update, genre for update
        """
        form = GenreForm()
        genre_to_update = cls.genres_service.get_genre(id)
        if request.method == "POST":
            try:
                cls.genres_service.update_genre(id, form.name.data, form.description.data)
                flash("Genre updated successfully!")
                return form, genre_to_update

            except:
                flash("Error! Looks like there was a problem! Try again...")
                return form, genre_to_update
        else:
            return form, genre_to_update
