"""
This module implements rendering add_book page
"""

from flask import render_template, flash
from bookstore_app import app, db
from bookstore_app.forms.book_form import BookForm
from bookstore_app.models.book_model import Book


@app.route('/edit_books', methods=['GET', 'POST'])
def edit_books():
    books = Book.query.order_by(Book.name)
    return render_template('edit_books.html', books=books)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = BookForm()

    if form.validate_on_submit():
        new_book = Book(name=form.name.data,
                        author_id=form.author_id.data,
                        genre_id=form.genre_id.data,
                        publish_date=form.publish_date.data,
                        description=form.description.data,
                        price=form.price.data,
                        rating=form.rating.data)
        # clear form
        form.name.data = ''
        form.author_id.data = ''
        form.genre_id.data = ''
        form.publish_date.data = ''
        form.description.data = ''
        form.price.data = ''
        form.rating.data = ''

        db.session.add(new_book)
        db.session.commit()

        flash('Book added successfuly!')

    return render_template('add_book.html', form=form)

