"""
This module implements rendering add_book page
"""

from flask import render_template
from bookstore_app import app
from bookstore_app.service.books_service import BooksService


books_service = BooksService()


@app.route("/books", methods=["GET"])
def books():
    """
    Returns rendered `books.html` template for url route
    `/books` and endpoint `books`

    :return: rendered `books.html` template
    """

    our_books = books_service.get_books()
    return render_template("books.html", books=our_books)


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    """
    Returns rendered `add_book.html` template for url route
    `/add_book` and endpoint `add_book`

    :return: rendered `add_book.html` template
    """
    form = books_service.add_book()
    return render_template("add_book.html", form=form)


@app.route("/delete_book/<int:id>", methods=["GET", "POST"])
def delete_book(id):
    """
    Returns rendered `books.html` template for url route
    `/delete_book/<int:id>` and endpoint `delete_book`

    :return: rendered `books.html` template
    """
    our_books = books_service.delete_book(id)

    return render_template("books.html",
                           books=our_books)


@app.route("/update_book/<int:id>", methods=["GET", "POST"])
def update_book(id):
    """
    Returns rendered `update_book.html` template for url route
    `/update_book/<int:id>` and endpoint `update_book`

    :return: rendered `update_book.html` template
    """
    form, book_to_update = books_service.update_book(id)
    return render_template("update_book.html",
                           form=form, book_to_update=book_to_update, id=id)


