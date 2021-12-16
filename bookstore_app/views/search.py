
from flask import render_template, request, redirect, url_for, flash
from bookstore_app import app

from bookstore_app.forms.search_form import SearchForm, RangeSearchForm

from bookstore_app.models.book_model import Book
from bookstore_app.models.genre_model import Genre
from bookstore_app.service.books_service import BooksService
from sqlalchemy import func

from datetime import date, datetime

book_service = BooksService()

# Pass Stuff To Navbar
@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)


# Create Search Function
@app.route("/books", methods=["POST"])
def search_books_by_name():
    form = SearchForm()
    if form.validate_on_submit():
        # query db
        page = request.args.get("page", 1, type=int)
        books = Book.query.filter(Book.name.like("%" + form.searched.data + "%")).\
            paginate(page=page, per_page=3, error_out=False)
        return render_template("books.html", form=form,
                               searched=form.searched.data, books=books)
    else:
        return redirect(url_for('books'))


@app.route("/books/<genre_name>", methods=["GET"])
def search_books_by_genre(genre_name):
    page = request.args.get("page", 1, type=int)

    searched_genre_id = Genre.query.with_entities(Genre.id).filter_by(name=genre_name)
    books = book_service.get_books().filter(Book.genre_id == searched_genre_id). \
        paginate(page=page, per_page=3, error_out=False)

    return render_template("books.html", books=books)


@app.route("/books/<int:id>", methods=["GET"])
def search_books_by_author(id):

    page = request.args.get("page", 1, type=int)
    books = book_service.get_books().filter(Book.author_id == id). \
        paginate(page=page, per_page=3, error_out=False)
    return render_template("books.html", books=books)




@app.route("/books/date", methods=["POST"])
def search_books_by_date():
    form = SearchForm()
    if form.validate_on_submit():
        # query db
        try:
            page = request.args.get("page", 1, type=int)
            books = Book.query.filter(Book.publish_date == datetime.
                                      strptime(form.searched.data, '%Y-%m-%d')).\
                paginate(page=page, per_page=3, error_out=False)
            return render_template("books.html", form=form,
                                   searched=form.searched.data, books=books)
        except ValueError:
            flash("Check your data please")
            return redirect(url_for('books'))
    else:
        return redirect(url_for('books'))


@app.route("/books/dates", methods=["POST"])
def search_books_by_dates():
    form = RangeSearchForm()
    if not form.searched_2.data:
        form.searched_2.data = str(date.today())
    if not form.searched_1.data:
        form.searched_1.data = str("1800-01-01")
    print(form.searched_2.data)
    if form.validate_on_submit():
        print('if')


        # query db
        page = request.args.get("page", 1, type=int)
        books = Book.query.filter(Book.publish_date >= datetime.strptime(form.searched_1.data, '%Y-%m-%d'))\
            .filter(Book.publish_date <= datetime.strptime(form.searched_2.data, '%Y-%m-%d'))\
            .paginate(page=page, per_page=3, error_out=False)
        return render_template("books.html", form=form, books=books)
    else:
        print('else')
        return redirect(url_for('books'))

#     .filter(User.birthday <= '1988-01-17').\
#         filter(User.birthday >= '1985-01-17')
