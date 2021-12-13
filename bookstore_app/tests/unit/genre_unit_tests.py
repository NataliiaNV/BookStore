import unittest
from unittest import TestCase
from unittest.mock import patch
from bookstore_app import app


def get_genres_mock():
    return []


class GenreTests(TestCase):

    @patch('bookstore_app.service.genres_service.GenresService.get_genres')
    def test_index(self, get_genres):
        get_genres.side_effect = get_genres_mock

        app.testing = True
        client = app.test_client()
        response = client.get('/genres')

        self.assertEqual(200, response.status_code)
        get_genres.assert_called_once()

if __name__ == "__main__":
    unittest.main()
