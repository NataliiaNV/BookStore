import unittest
from unittest import TestCase, mock
from bookstore_app import app
from bookstore_app.forms.author_form import AuthorForm
from bs4 import BeautifulSoup

from datetime import date, datetime

def get_authors_mock():
    return [], {}


def add_author_mock():
    form = AuthorForm()
    form.name.data = "NV"
    form.birth_date.data = "1995-12-24"
    return form


def delete_author_mock(id):
    return [], {}


def update_author_mock(id):
    form = AuthorForm()
    form.name.data = "NV"
    form.birth_date.data = datetime.strptime("1995-12-24", "%Y-%m-%d")
    author_to_update = {"id": id, "name": "Nata", "birth_date": datetime.strptime("1995-12-23", "%Y-%m-%d")}
    return form, author_to_update


class AuthorTests(TestCase):

    @mock.patch("bookstore_app.service.authors_service.AuthorsService.get_authors")
    def test_authors(self, get_authors):
        get_authors.side_effect = get_authors_mock

        app.testing = True
        client = app.test_client()
        response = client.get("/authors")

        self.assertEqual(200, response.status_code)
        get_authors.assert_called_once()

    @mock.patch("bookstore_app.service.authors_service.AuthorsService.add_author")
    def test_add_author(self, add_author):
        with app.test_request_context():
            add_author.side_effect = add_author_mock

            add_author_mock_data = add_author_mock()

        app.testing = True
        client = app.test_client()
        response = client.get("/add_author")



        soup = BeautifulSoup(response.data, "html.parser")
        form_name = soup.find("input", {"name": "name"})["value"]
        form_birth_date = soup.find("input", {"name": "birth_date"})["value"]

        self.assertEqual(200, response.status_code)
        add_author.assert_called_once()

        self.assertEqual(add_author_mock_data.name.data, form_name)
        self.assertEqual(add_author_mock_data.birth_date.data, form_birth_date)

    @mock.patch("bookstore_app.service.authors_service.AuthorsService.delete_author")
    def test_delete_author(self, delete_author):
        delete_author.side_effect = delete_author_mock
        id = 1

        app.testing = True
        client = app.test_client()

        response = client.get("/delete_author/" + str(id))

        self.assertEqual(200, response.status_code)
        delete_author.assert_called_once()
        delete_author.assert_called_with(id)

    @mock.patch("bookstore_app.service.authors_service.AuthorsService.update_author")
    def test_update_genre(self, update_author):
        update_author.side_effect = update_author_mock
        id = 1

        app.testing = True
        client = app.test_client()

        response = client.get("/update_author/" + str(id))

        self.assertEqual(200, response.status_code)
        update_author.assert_called_once()
        update_author.assert_called_with(id)


if __name__ == "__main__":
    unittest.main()
