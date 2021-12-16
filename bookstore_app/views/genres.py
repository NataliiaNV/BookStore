"""
This module implements rendering  genre page
"""

from flask import render_template
from bookstore_app import app
from bookstore_app.service.genres_service import GenresService

genres_service = GenresService()


@app.route('/genres', methods=['GET'])
def genres():
    genres = genres_service.get_genres()
    return render_template('genres.html', genres=genres)


@app.route('/add_genre', methods=['GET', 'POST'])
def add_genre():
    form = genres_service.add_genre()
    return render_template('add_genre.html', form=form)


@app.route('/delete_genre/<int:id>')
def delete_genre(id):
    form, genres = genres_service.delete_genre(id)
    return render_template('genres.html', form=form, genres=genres)


@app.route('/update_genre/<int:id>', methods=['GET', 'POST'])
def update_genre(id):
    form, genre_to_update = genres_service.update_genre(id)
    return render_template("update_genre.html",
                           form=form, genre_to_update=genre_to_update, id=id)
