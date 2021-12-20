"""
This module implements unittests for books
"""

import unittest
from unittest import TestCase, mock
from bookstore_app import app
from bookstore_app.forms.book_form import BookForm
from bs4 import BeautifulSoup

from datetime import datetime


def get_books_mock():
    """
    Return datas for testing get_books
    """
    return []


def add_book_mock():
    """
    Return form for testing add_book
    """
    form = BookForm()
    form.name.data = "Harry"
    form.author_id.data = 1
    form.genre_id.data = 1
    form.publish_date.data = "1995-12-24"
    form.description.data = " It is book about Harry"
    form.price.data = "420"
    form.rating.data = "8"
    return form


def delete_book_mock(id):
    """
    Return datas for testing delete_book
    """
    return []


def update_book_mock(id):
    """
    Return datas for testing update_book
    """
    form = BookForm()
    form.name.data = "Harry"
    form.author_id.data = 1
    form.genre_id.data = 1
    form.publish_date.data = datetime.strptime("1995-12-24", "%Y-%m-%d")
    form.description.data = "It is book about Harry"
    form.price.data = "420"
    form.rating.data = "8"

    book_to_update = {"id": id, "name": "Lidia", "author_id": 2, "genre_id": 2,
                      "publish_date": datetime.strptime("1995-12-23", "%Y-%m-%d"),
                      "description": "It is book about Lidia",
                      "price": "600", "rating": "5"}
    return form, book_to_update


class BookTests(TestCase):
    """
    This class implements tests for books
    """

    @mock.patch("bookstore_app.service.books_service.BooksService.get_books")
    def test_books(self, get_authors):
        """
        Tests get_books
        """
        get_authors.side_effect = get_books_mock

        app.testing = True
        client = app.test_client()
        response = client.get("/books")

        self.assertEqual(200, response.status_code)
        get_authors.assert_called_once()

    @mock.patch("bookstore_app.service.books_service.BooksService.add_book")
    def test_add_author(self, add_book):
        """
        Tests add_book
        """
        with app.test_request_context():
            add_book.side_effect = add_book_mock

            add_book_mock_data = add_book_mock()

        app.testing = True
        client = app.test_client()
        response = client.get("/add_book")

        soup = BeautifulSoup(response.data, "html.parser")
        form_name = soup.find("input", {"name": "name"})["value"]
        form_publish_date = soup.find("input", {"name": "publish_date"})["value"]
        form_description = soup.find("input", {"name": "description"})["value"]
        form_price = soup.find("input", {"name": "price"})["value"]
        form_rating = soup.find("input", {"name": "rating"})["value"]

        self.assertEqual(200, response.status_code)
        add_book.assert_called_once()

        self.assertEqual(add_book_mock_data.name.data, form_name)
        self.assertEqual(add_book_mock_data.publish_date.data, form_publish_date)
        self.assertEqual(add_book_mock_data.description.data, form_description)
        self.assertEqual(add_book_mock_data.price.data, form_price)
        self.assertEqual(add_book_mock_data.rating.data, form_rating)

    @mock.patch("bookstore_app.service.books_service.BooksService.delete_book")
    def test_delete_book(self, delete_book):
        """
          Tests delete_book
        """
        delete_book.side_effect = delete_book_mock
        id = 1

        app.testing = True
        client = app.test_client()

        response = client.get("/delete_book/" + str(id))

        self.assertEqual(200, response.status_code)
        delete_book.assert_called_once()
        delete_book.assert_called_with(id)

    @mock.patch("bookstore_app.service.books_service.BooksService.update_book")
    def test_update_book(self, update_book):
        """
          Tests update_book
        """
        update_book.side_effect = update_book_mock
        id = 1

        app.testing = True
        client = app.test_client()

        response = client.get("/update_book/" + str(id))

        self.assertEqual(200, response.status_code)
        update_book.assert_called_once()
        update_book.assert_called_with(id)


if __name__ == "__main__":
    unittest.main()
