import sqlalchemy

from flask import flash, request
from bookstore_app import app, db
from flask import flash, request
from bookstore_app.forms.book_form import BookForm
from bookstore_app.models.book_model import Book
from bookstore_app.models.genre_model import Genre
from bookstore_app.models.author_model import Author


class BooksService:

    @classmethod
    def get_books(cls):
        page = request.args.get('page', 1, type=int)
        our_books = Book.query.join(Genre, Genre.id == Book.genre_id).\
            join(Author, Author.id == Book.author_id)\
            .add_columns(Book.id, Book.name, Book.author_id, Book.rating,
                         Book.price, Author.name.label("author_name"),
                         Book.description, Book.publish_date, Genre.name.label("genres_name"))\
            .paginate(page=page, per_page=3, error_out=False)

        return our_books



    @classmethod
    def add_book(cls):
        form = BookForm()
        try:
            if form.name.data is None or form.name.data == "":
                flash("Fill in the data please!")
            elif form.validate_on_submit():
                new_book = Book(name=form.name.data,
                                author_id=form.author_id.data,
                                genre_id=form.genre_id.data,
                                publish_date=form.publish_date.data,
                                description=form.description.data,
                                price=form.price.data,
                                rating=form.rating.data)


                db.session.add(new_book)
                db.session.commit()

                # clear form
                form.name.data = ''
                form.author_id.data = ''
                form.genre_id.data = ''
                form.publish_date.data = ''
                form.description.data = ''
                form.price.data = ''
                form.rating.data = ''

                flash('Book added successfuly!')
        except sqlalchemy.exc.IntegrityError:
            flash("Check please your data!")
        except sqlalchemy.exc.OperationalError:
            flash("Check formats please!")

        return form

    @classmethod
    def delete_book(cls, id):
        book_to_delete = Book.query.get_or_404(id)
        form = BookForm()

        try:
            db.session.delete(book_to_delete)
            db.session.commit()
            flash("Book deleted successfully!")
            our_books = Book.query.order_by(Book.id)
            return form, our_books
        except:
            flash("Oops! There was a problem with deleting book, try again...")
            return form, our_books

    @classmethod
    def update_book(cls, id):
        form = BookForm()
        book_to_update = Book.query.get_or_404(id)
        if request.method == 'POST':
            book_to_update.name = request.form['name']
            book_to_update.author_id = request.form['author_id']
            book_to_update.genre_id = request.form['genre_id']
            book_to_update.publish_date = request.form['publish_date']
            book_to_update.description = request.form['description']
            book_to_update.price = request.form['price']
            book_to_update.rating = request.form['rating']
            try:
                db.session.commit()
                flash("Book updated successfuly!")
                return form, book_to_update
            except:
                flash("Error! Looks like there was a problem! Try again...")
                return form, book_to_update
        else:
            return form, book_to_update
