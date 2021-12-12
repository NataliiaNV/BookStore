"""
This module implements rendering author page
"""

from flask import render_template
from bookstore_app import app
from bookstore_app.service.authors_service import AuthorsService

authors_service = AuthorsService()


@app.route('/authors', methods=['GET', 'POST'])
def authors():
    authors, avg_rate = authors_service.get_authors()
    return render_template('authors.html', authors=authors, avg_rate=avg_rate)


@app.route('/add_authors', methods=['GET', 'POST'])
def add_author():
    form = authors_service.add_author()
    return render_template('add_author.html', form=form)


@app.route('/update_author/<int:id>', methods=['GET', 'POST'])
def update_author(id):
    form, author_to_update = authors_service.update_author(id)
    return render_template("update_author.html",
                           form=form, author_to_update=author_to_update, id=id)


@app.route('/delete_author/<int:id>')
def delete_author(id):
    form, authors = authors_service.delete_author(id)
    return render_template('edit_authors.html', form=form, authors=authors)

