import sqlalchemy

from bookstore_app.models.genre_model import Genre
from bookstore_app.forms.genre_form import GenreForm
from bookstore_app.models.book_model import Book
from bookstore_app import db
from flask import flash, request


class GenresService:

    @classmethod
    def get_genres(cls):
        return Genre.query.order_by(Genre.id)

    @classmethod
    def add_genre(cls):
        form = GenreForm()
        try:
            if form.name.data is None or form.name.data == "":
                flash("Fill in the data please!")
            elif form.validate_on_submit():
                new_genre = Genre(name=form.name.data,
                                  description=form.description.data)
                # clear form
                form.name.data = ''
                form.description.data = ''

                db.session.add(new_genre)
                db.session.commit()

                flash("Genre added successfully!")
        except sqlalchemy.exc.IntegrityError:
            flash("This genre already exists!")

        return form

    @classmethod
    def delete_genre(cls, id):
        genre_to_delete = Genre.query.get_or_404(id)
        form = GenreForm()

        if not db.session.query(
                db.session.query(Book).filter_by(genre_id=id).exists()).scalar():
            try:
                db.session.delete(genre_to_delete)
                db.session.commit()
                flash("Genre deleted successfully!")
                genres = Genre.query.order_by(Genre.id)
                return form, genres
            except:
                flash("Oops! There was a problem with deleting genre, try again...")
                return form, genres
        else:
            genres = Genre.query.order_by(Genre.id)
            flash("Sorry, you can't delete this genre, you have books of this genre!")
            return form, genres


    @classmethod
    def update_genre(cls, id):
        form = GenreForm()
        genre_to_update = Genre.query.get_or_404(id)
        if request.method == 'POST':
            genre_to_update.name = request.form['name']
            genre_to_update.description = request.form['description']
            try:
                db.session.commit()
                flash("Genre updated successfully!")
                return form, genre_to_update
            except:
                flash("Error! Looks like there was a problem! Try again...")
                return form, genre_to_update
        else:
            return form, genre_to_update
