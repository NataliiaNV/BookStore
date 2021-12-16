"""
This module implements rendering add_book page
"""

from flask import render_template, flash, request
from bookstore_app import app, db
from bookstore_app.forms.book_form import BookForm
from bookstore_app.models.book_model import Book
from bookstore_app.service.books_service import BooksService

books_service = BooksService()

@app.route('/books', methods=['GET', 'POST'])
def books():
    page = request.args.get('page', 1, type=int)
    our_books = books_service.get_books().paginate(page=page, per_page=3, error_out=False)
    return render_template('books.html', books=our_books)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = books_service.add_book()
    return render_template('add_book.html', form=form)


@app.route('/delete_book/<int:id>')
def delete_book(id):
    form, our_books = books_service.delete_book(id)
    return render_template('books.html',
                           form=form, books=our_books)


@app.route('/update_book/<int:id>', methods=['GET', 'POST'])
def update_book(id):
    form, book_to_update = books_service.update_book(id)
    return render_template("update_book.html",
                           form=form, book_to_update=book_to_update, id=id)


