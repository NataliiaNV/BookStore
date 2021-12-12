import unittest
from bookstore import app

from views import home, search, genres, authors, books


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




if __name__ == "__main__":
    unittest.main()

