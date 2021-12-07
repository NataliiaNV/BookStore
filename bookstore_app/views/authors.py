"""
This module implements rendering add_genre page
"""

from flask import render_template, flash
from bookstore_app import app, db
from bookstore_app.forms.author_form import AuthorForm
from bookstore_app.models.author_model import Author


@app.route('/edit_authors', methods=['GET', 'POST'])
def edit_authors():
    authors = Author.query.order_by(Author.id)
    return render_template('edit_authors.html', authors=authors)


@app.route('/add_authors', methods=['GET', 'POST', 'PUT'])
def add_author():
    form = AuthorForm()

    if form.validate_on_submit():
        new_auth = Author(name=form.name.data,
                          birth_date=form.birth_date.data)
        # clear form
        form.name.data = ''
        form.birth_date.data = ''


        # add post data to db
        db.session.add(new_auth)
        db.session.commit()

        flash('Author added successfuly!')

    return render_template('add_author.html', form=form)

