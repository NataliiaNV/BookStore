"""
This package contains modules defining authors, books, genres, home and search services:

Modules:

- `authors.py`: defines authors views
- `books.py`: defines books views
- `genres.py`: defines genres views
- `home.py`: defines homepage views
- `search.py`: defines search views
"""

from bookstore_app import app

from . import authors
from . import books
from . import genres
from . import home
from . import search

