"""
This module implements rendering  genre page
"""

from flask import render_template, flash, request
from bookstore import app, db
from forms.genre_form import GenreForm
from models.genre_model import Genre


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


@app.route('/delete_genre/<int:id>')
def delete_genre(id):
    genre_to_delete = Genre.query.get_or_404(id)
    form = GenreForm()

    try:
        db.session.delete(genre_to_delete)
        db.session.commit()
        flash("Genre deleted successfully!")
        genres = Genre.query.order_by(Genre.id)
        return render_template('edit_genres.html',
                               form=form,
                               genres=genres)
    except:
        flash("Oops! There was a problem with deleting genre, try again...")
        return render_template('edit_genres.html',
                               form=form,
                               genres=genres)


@app.route('/update_genre/<int:id>', methods=['GET', 'POST'])
def update_genre(id):
    form = GenreForm()
    genre_to_update = Genre.query.get_or_404(id)
    if request.method == 'POST':
        genre_to_update.name = request.form['name']
        genre_to_update.description = request.form['description']
        try:
            db.session.commit()
            flash("Genre updated successfuly!")
            return render_template("update_genre.html",
                                   form=form, genre_to_update=genre_to_update)
        except:
            flash("Error! Looks like there was a problem! Try again...")
            return render_template("update_genre.html",
                                   form=form, genre_to_update=genre_to_update)
    else:
        return render_template("update_genre.html",
                               form=form, genre_to_update=genre_to_update, id=id)
