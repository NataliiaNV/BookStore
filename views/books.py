"""
This module implements rendering add_book page
"""

from flask import render_template, flash, request
from bookstore import app, db
from forms.book_form import BookForm
from models.book_model import Book


@app.route('/books', methods=['GET', 'POST'])
def books():
    page = request.args.get('page', 1, type=int)
    our_books = Book.query.order_by(Book.id).paginate(page=page, per_page=2, error_out=False)
    return render_template('books.html', books=our_books)


@app.route('/edit_books', methods=['GET', 'POST'])
def edit_books():
    our_books = Book.query.order_by(Book.name)
    return render_template('edit_books.html', books=our_books)


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


@app.route('/delete_book/<int:id>')
def delete_book(id):
    book_to_delete = Book.query.get_or_404(id)
    form = BookForm()

    try:
        db.session.delete(book_to_delete)
        db.session.commit()
        flash("Genre deleted successfully!")
        our_books = Book.query.order_by(Book.id)
        return render_template('edit_books.html',
                               form=form,
                               books=our_books)
    except:
        flash("Oops! There was a problem with deleting book, try again...")
        return render_template('edit_books.html',
                               form=form,
                               books=our_books)


@app.route('/update_book/<int:id>', methods=['GET', 'POST'])
def update_book(id):
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
            return render_template("update_book.html",
                                   form=form, book_to_update=book_to_update)
        except:
            flash("Error! Looks like there was a problem! Try again...")
            return render_template("update_book.html",
                                   form=form, book_to_update=book_to_update)
    else:
        return render_template("update_book.html",
                               form=form, book_to_update=book_to_update, id=id)

