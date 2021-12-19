"""
This module implements services for author, used to make database queries
"""


import sqlalchemy


from bookstore_app import db
from bookstore_app.forms.author_form import AuthorForm
from bookstore_app.models.author_model import Author
from bookstore_app.models.book_model import Book
from flask import flash, request
from datetime import datetime


class AuthorsService:
    """
    This class implements services for authors, used to make database queries
    """

    @classmethod
    def __avg_rate(cls):
        """
        Calculate avg_rate rating for authors based on theirs books
        :param avg_rate: rating for authors based on theirs books
        :return: avg_rate
        """
        avg_rate = db.session.query(Author.id, db.func.round(db.func.avg(Book.rating), 2)). \
            join(Author).group_by(Author.id).all()

        return avg_rate

    @classmethod
    def get_authors(cls):
        """
        Fetches all authors from database and paging it
        :param avg_rate: rating for authors based on theirs books
        :return: list of all authors, dict(avg_rate)
        """
        avg_rate = cls.__avg_rate()
            # db.session.query(Author.id, db.func.round(db.func.avg(Book.rating), 2)). \
            # join(Author).group_by(Author.id).all()
        our_authors = Author.query.order_by(Author.id)
        return our_authors, dict(avg_rate)


    @classmethod
    def add_author(cls):
        """
        Add new author to database
        :param form: form for posting new author's data
        :return: form
        """
        form = AuthorForm()

        try:
            if form.name.data is None or form.name.data == "":
                flash("Fill in the data please!")
            elif datetime.strptime(form.birth_date.data, "%Y-%m-%d") > datetime.today():
                flash("Please choose the correct date!")
            elif form.validate_on_submit():
                new_auth = Author(name=form.name.data,
                                  birth_date=form.birth_date.data)


                db.session.add(new_auth)
                db.session.commit()

                # clear form
                form.name.data = ""
                form.birth_date.data = ""

                flash("Author added successfully!")
        except sqlalchemy.exc.IntegrityError:
            flash("This author already exists!")
        except sqlalchemy.exc.OperationalError:
            flash("Check the data format!")

        return form

    @classmethod
    def delete_author(cls, id):
        """
        Delete author by id, and fetches other authors from database and paging it
        :param id: the id of the author we want to delete
        :return: all authors in the database, except which we delete, avg_rate rating for authors based on their books
        """
        author_to_delete = Author.query.get_or_404(id)

        if not db.session.query(
                db.session.query(Book).filter_by(author_id=id).exists()).scalar():
            try:
                db.session.delete(author_to_delete)
                db.session.commit()
                flash("Author deleted successfully!")

                our_authors, dict_avg_rate = cls.get_authors()

                return our_authors, dict_avg_rate
            except:
                flash("Oops! There was a problem with deleting author, try again...")
                return our_authors, dict_avg_rate
        else:
            our_authors, dict_avg_rate = cls.get_authors()
            flash("Sorry, you can't delete this author, you have books by this author!")
            return our_authors, dict_avg_rate

    @classmethod
    def update_author(cls, id):
        """
        Update author by id
        :param form: form for updating author's data
        :param author_to_update: author that we want to update(get by id)
        :return: form with fields for update, author for update
        """
        form = AuthorForm()
        author_to_update = Author.query.get_or_404(id)
        if request.method == "POST":
            author_to_update.name = request.form["name"]
            author_to_update.birth_date = request.form["birth_date"]
            try:
                db.session.commit()
                flash("Author updated successfuly!")
                return form, author_to_update
            except:
                flash("Error! Looks like there was a problem! Try again...")
                return form, author_to_update
        else:
            return form, author_to_update





