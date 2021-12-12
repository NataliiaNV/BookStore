"""
This module implements rendering author page
"""

from flask import render_template, flash, request
from bookstore import app, db
from forms.author_form import AuthorForm
from models.author_model import Author
from models.book_model import Book


@app.route('/authors', methods=['GET', 'POST'])
def authors():
    page = request.args.get('page', 1, type=int)
    avg_rate = db.session.query(Author.id, db.func.round(db.func.avg(Book.rating), 2)). \
        join(Author).group_by(Author.id).all()
    our_authors = Author.query.order_by(Author.id).paginate(page=page, per_page=5, error_out=False)

    return render_template('authors.html', authors=our_authors, avg_rate=dict(avg_rate))


@app.route('/edit_authors', methods=['GET', 'POST'])
def edit_authors():
    our_authors = Author.query.order_by(Author.id)
    return render_template('edit_authors.html', authors=our_authors)


@app.route('/add_authors', methods=['GET', 'POST'])
def add_author():
    form = AuthorForm()

    if form.validate_on_submit():
        new_auth = Author(name=form.name.data,
                          birth_date=form.birth_date.data)
        # clear form
        form.name.data = ''
        form.birth_date.data = ''

        db.session.add(new_auth)
        db.session.commit()

        flash('Author added successfuly!')

    return render_template('add_author.html', form=form)


@app.route('/delete_author/<int:id>')
def delete_author(id):
    author_to_delete = Author.query.get_or_404(id)
    form = AuthorForm()

    try:
        db.session.delete(author_to_delete)
        db.session.commit()
        flash("Author deleted successfully!")
        our_authors = Author.query.order_by(Author.id)
        return render_template('edit_authors.html',
                               form=form,
                               authors=our_authors)
    except:
        flash("Oops! There was a problem with deleting author, try again...")
        return render_template('edit_authors.html',
                               form=form,
                               authors=our_authors)


@app.route('/update_author/<int:id>', methods=['GET', 'POST'])
def update_author(id):
    form = AuthorForm()
    author_to_update = Author.query.get_or_404(id)
    if request.method == 'POST':
        author_to_update.name = request.form['name']
        author_to_update.birth_date = request.form['birth_date']
        try:
            db.session.commit()
            flash("Author updated successfuly!")
            return render_template("update_author.html",
                                   form=form, author_to_update=author_to_update)
        except:
            flash("Error! Looks like there was a problem! Try again...")
            return render_template("update_author.html",
                                   form=form, author_to_update=author_to_update)
    else:
        return render_template("update_author.html",
                               form=form, author_to_update=author_to_update, id=id)
