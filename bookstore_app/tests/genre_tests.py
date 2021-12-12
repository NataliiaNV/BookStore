import unittest
from bookstore_app import app


class GenreTests(unittest.TestCase):

    """ Check for response 200"""
    def test_index(self):
        app.testing = True
        client = app.test_client()
        response = client.get('/')
        statuscode = response.status_code
        # for rule in app.url_map.iter_rules():
        #     print(rule)
        self.assertEqual(200, statuscode)

    def test_edit_genres(self):
        app.testing = True
        client = app.test_client()
        response = client.get('/edit_genres')

        self.assertEqual(200, response.status_code)
        #self.assertEqual(response.data, )


if __name__ == "__main__":
    unittest.main()

