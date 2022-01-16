"""
This module implements rendering author page
"""

from flask import render_template
from bookstore_app import app
from bookstore_app.controllers.authors_controller import AuthorsController

authors_controller = AuthorsController()

@app.route("/authors", methods=["GET", "POST"])
def authors():
    """
    Returns rendered `authors.html` template for url route
    `/authors` and endpoint `authors`

    :return: rendered `authors.html` template
    """
    authors, avg_rate = authors_controller.get_authors()
    return render_template("authors.html", authors=authors, avg_rate=avg_rate)


@app.route("/add_author", methods=["GET", "POST"])
def add_author():
    """
    Returns rendered `add_author.html` template for url route
    `/add_author` and endpoint `add_author`

    :return: rendered `add_author.html` template
    """

    form = authors_controller.add_author()
    return render_template("add_author.html", form=form)


@app.route("/update_author/<int:id>", methods=["GET", "POST"])
def update_author(id):
    """
    Returns rendered `update_author.html` template for url route
    `/update_author/<int:id>` and endpoint `update_author`

    :return: rendered `update_author.html` template
    """
    form, author_to_update = authors_controller.update_author(id)
    return render_template("update_author.html",
                           form=form, author_to_update=author_to_update, id=id)


@app.route("/delete_author/<int:id>")
def delete_author(id):
    """
    Returns rendered `authors.html` template for url route
    `/delete_author/<int:id>` and endpoint `delete_author`

    :return: rendered `authors.html` template
    """
    authors, avg_rate = authors_controller.delete_author(id)

    return render_template("authors.html", authors=authors, avg_rate=avg_rate)

