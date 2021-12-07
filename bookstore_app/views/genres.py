"""
This module implements rendering add_genre page
"""

from flask import render_template, flash
from bookstore_app import app, db
from bookstore_app.forms.genre_form import GenreForm
from bookstore_app.models.genre_model import Genre


@app.route('/edit_genres', methods=['GET', 'POST'])
def edit_genres():
    genres = Genre.query.order_by(Genre.id)
    return render_template('edit_genres.html', genres=genres)


@app.route('/add_genre', methods=['GET', 'POST', 'PUT'])
def add_genre():
    form = GenreForm()

    if form.validate_on_submit():
        new_genre = Genre(name=form.name.data,
                          description=form.description.data)
        # clear form
        form.name.data = ''
        form.description.data = ''

        db.session.add(new_genre)
        db.session.commit()

        flash('Genre added successfuly!')

    return render_template('add_genre.html', form=form)

