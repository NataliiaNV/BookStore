"""
This module implements services for books, used to make database queries
"""
from bookstore_app import db
from bookstore_app.models.book_model import Book
from bookstore_app.models.genre_model import Genre
from bookstore_app.models.author_model import Author


class BooksService:
    """
    This class implements services for books, used to make database queries
    """

    @classmethod
    def get_books(cls):
        """
        Fetches all books from database
        :return: our_books
        """
        our_books = Book.query.join(Genre, Genre.id == Book.genre_id). \
            join(Author, Author.id == Book.author_id) \
            .add_columns(Book.id, Book.name, Book.author_id, Book.rating,
                         Book.price, Book.author_id, Book.genre_id, Book.description,
                         Book.publish_date, Genre.name.label("genres_name"), Author.name.label("author_name"))

        return our_books

    @classmethod
    def get_books_api(cls):
        """
        Fetches all books from database
        :return: our_books
        """
        books = Book.query.all()

        return books

    @classmethod
    def get_book(cls, id):
        """
        Fetches book from database
        :param id: book id
        :return: our_book
        """
        our_book = Book.query.get_or_404(id)

        return our_book

    @classmethod
    def add_book(cls, name, author_id, genre_id, publish_date, description, price, rating):
        """
        Add new book to database
        :param name: book name
        :param author_id: author id
        :param genre_id:  genre id
        :param publish_date: publish date
        :param description: description
        :param price: book's price
        :param rating: book's rating
        :return: form
        """
        new_book = Book(name=name,
                        author_id=author_id,
                        genre_id=genre_id,
                        publish_date=publish_date,
                        description=description,
                        price=price,
                        rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return None

    @classmethod
    def delete_book(cls, id):
        """
        Delete author by id, and fetches other authors from database and paging it
        :param id: book id
        :return: all books in the database, except which we delete
        """
        book_to_delete = Book.query.get_or_404(id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return None

    @classmethod
    def update_book(cls, id, name, author_id, genre_id, publish_date, description, price, rating):
        """
        Update book by id
        :param id: book id
        :param name: book name
        :param author_id: author id
        :param genre_id: genre id
        :param publish_date: publish date
        :param description: book description
        :param price: book price
        :param rating: bookrating
        :param book_to_update: book that we want to update(get by id)
        :return: None
        """
        book_to_update = Book.query.get_or_404(id)

        if name:
            book_to_update.name = name
        if author_id:
            book_to_update.author_id = author_id
        if genre_id:
            book_to_update.genre_id = genre_id
        if publish_date:
            book_to_update.publish_date = publish_date
        if description:
            book_to_update.description = description
        if price:
            book_to_update.price = price
        if rating:
            book_to_update.rating = rating

        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise Exception

        return None
