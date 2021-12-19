import unittest
from unittest import TestCase, mock
from bookstore_app import app
from bookstore_app.forms.genre_form import GenreForm
from bs4 import BeautifulSoup



def get_genres_mock():
    return []


def add_genre_mock():
    form = GenreForm()
    form.name.data = "Fantasy"
    form.description.data = "It is fantasy."
    return form


def delete_genre_mock(id):
    return []


def update_genre_mock(id):
    form = GenreForm()
    form.name.data = "Fantasy"
    form.description.data = "It is fantasy."
    genre_to_update = {"id": id, "name": "Classics", "description": "It is classics."}
    return form, genre_to_update


class GenreTests(TestCase):

    @mock.patch("bookstore_app.service.genres_service.GenresService.get_genres")
    def test_genres(self, get_genres):
        get_genres.side_effect = get_genres_mock

        app.testing = True
        client = app.test_client()
        response = client.get("/genres")

        self.assertEqual(200, response.status_code)
        get_genres.assert_called_once()

    @mock.patch("bookstore_app.service.genres_service.GenresService.add_genre")
    def test_add_genres(self, add_genre):
        with app.test_request_context():
            add_genre.side_effect = add_genre_mock

            add_genre_mock_data = add_genre_mock()

        app.testing = True
        client = app.test_client()
        response = client.get("/add_genre")

        soup = BeautifulSoup(response.data, "html.parser")
        form_name = soup.find("input", {"name": "name"})["value"]
        form_description = soup.find("input", {"name": "description"})["value"]

        self.assertEqual(200, response.status_code)
        add_genre.assert_called_once()
        self.assertEqual(add_genre_mock_data.name.data, form_name)
        self.assertEqual(add_genre_mock_data.description.data, form_description)

    @mock.patch("bookstore_app.service.genres_service.GenresService.delete_genre")
    def test_delete_genre(self, delete_genre):
        delete_genre.side_effect = delete_genre_mock
        id = 1

        app.testing = True
        client = app.test_client()

        response = client.get("/delete_genre/" + str(id))

        self.assertEqual(200, response.status_code)
        delete_genre.assert_called_once()
        delete_genre.assert_called_with(id)

    @mock.patch("bookstore_app.service.genres_service.GenresService.update_genre")
    def test_update_genre(self, update_genre):
        update_genre.side_effect = update_genre_mock
        id = 1

        app.testing = True
        client = app.test_client()

        response = client.get("/update_genre/" + str(id))

        self.assertEqual(200, response.status_code)
        update_genre.assert_called_once()
        update_genre.assert_called_with(id)


if __name__ == "__main__":
    unittest.main()
