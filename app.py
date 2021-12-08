from bookstore_app import app
from bookstore_app.views import home, genres, authors, books, search

if __name__ == '__main__':
    app.run(debug=True)




