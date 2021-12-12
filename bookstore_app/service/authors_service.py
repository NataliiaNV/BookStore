import sqlalchemy


from bookstore_app import db
from bookstore_app.forms.author_form import AuthorForm
from bookstore_app.models.author_model import Author
from bookstore_app.models.book_model import Book
from flask import flash, request


class AuthorsService:

    @classmethod
    def get_authors(cls):
        page = request.args.get('page', 1, type=int)
        avg_rate = db.session.query(Author.id, db.func.round(db.func.avg(Book.rating), 2)). \
            join(Author).group_by(Author.id).all()
        our_authors = Author.query.order_by(Author.id).paginate(page=page, per_page=5, error_out=False)
        return our_authors, dict(avg_rate)


    @classmethod
    def add_author(cls):
        form = AuthorForm()

        try:
            if form.name.data is None or form.name.data == "":
                flash("Fill in the data please!")
            elif form.validate_on_submit():
                new_auth = Author(name=form.name.data,
                                  birth_date=form.birth_date.data)
                # clear form
                form.name.data = ''
                form.birth_date.data = ''

                db.session.add(new_auth)
                db.session.commit()

                flash("Author added successfully!")
        except sqlalchemy.exc.IntegrityError:
            flash("This author already exists!")

        return form

    @classmethod
    def delete_author(cls, id):
        author_to_delete = Author.query.get_or_404(id)
        form = AuthorForm()

        try:
            db.session.delete(author_to_delete)
            db.session.commit()
            flash("Author deleted successfully!")
            our_authors = Author.query.order_by(Author.id)
            return form, our_authors
        except:
            flash("Oops! There was a problem with deleting author, try again...")
            return form, our_authors

    @classmethod
    def update_author(cls, id):
        form = AuthorForm()
        author_to_update = Author.query.get_or_404(id)
        if request.method == 'POST':
            author_to_update.name = request.form['name']
            author_to_update.birth_date = request.form['birth_date']
            try:
                db.session.commit()
                flash("Author updated successfuly!")
                return form, author_to_update
            except:
                flash("Error! Looks like there was a problem! Try again...")
                return form, author_to_update
        else:
            return form, author_to_update





