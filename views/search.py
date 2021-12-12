
from flask import render_template, flash, request
from bookstore import app

from forms.search_form import SearchForm

from models.genre_model import Genre
from models.author_model import Author
from models.book_model import Book


# Pass Stuff To Navbar
@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)


# Create Search Function
@app.route('/search', methods=["POST"])
def search():
    form = SearchForm()

    if form.validate_on_submit():
        # query db
        page = request.args.get('page', 1, type=int)
        books = Book.query.filter(Book.name.like('%' + form.searched.data + '%')).\
            paginate(page=page, per_page=3, error_out=False)
        return render_template("books.html", form=form,
                               searched=form.searched.data, books=books)



