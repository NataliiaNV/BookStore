# BookStore
## Flask project simple web application

This project was created as the first step of an online bookstore to manage books and their authors, genres through a web application or with a help of REST API. It reads and writes data to a MySQL database. With this program you can:

- create, update and delete books, authors and genres
- search for books published between two dates or a specific date
- search for books by genre, author, or title
- calculate the average rating of authors based on the rating of their books

## Structure

- forms - this package includes modules with forms for html templates
- models - this package includes modules with Python classes describing DB models
- rest - this package includes modules with REST API implementation
- service - this package includes modules with functions to work with DB  
- templates - html templates
- controllers - this package include modules with Web controllers 
- tests - this package includes modules with unit and integration tests
- views - this package includes modules views

## Instalation

1. Clone this repo.

```
git clone https://github.com/NataliiaNV/BookStore
```

2. Set up and activate the virtual environment (optionally).

```
virtualenv venv
source env/bin/activate
```

3. Install the requirements.

```
pip install -r requirements.txt
```

4. Configure MySQL database.

```
export MYSQL_USER=root
export MYSQL_PASSWORD=password
export MYSQL_SERVER=localhost
export MYSQL_DATABASE=bookstore
```

5. Create database.

```
python bookstore_app/sql/create_db.py
```

6.Run migrations to create database infrastructure.

```
flask db upgrade
```

7. Populate database.

```
python -m bookstore_app.sql.populate_db
```

8. Run the project locally.

```
flask run
```
or
```
python app.py
```

## Web app tabs

This is the main page of Web app. 
![Alt-текст](https://github.com/NataliiaNV/BookStore/blob/main/documentation/img/home.png "home") 

This is the page on which genres could be viewed, added, edited and deleted.
![Alt-текст](https://github.com/NataliiaNV/BookStore/blob/main/documentation/img/genres.png "home")

This is the page on which authors could be viewed, added, edited and deleted.
![Alt-текст](https://github.com/NataliiaNV/BookStore/blob/main/documentation/img/authors.png "home")

This is the page on which books could be viewed, added, edited and deleted.
Here you can search the book by name and on the left top corner.
The book could be also searched by the publish date using specific date or range of dates.
![Alt-текст](https://github.com/NataliiaNV/BookStore/blob/main/documentation/img/books.png "home")

##  REST API requests

- **localhost:5000/api/genres**
  - ***GET*** - return all genres
  - ***POST*** - create new genre
    ```
    {
    "description": "When a book has stood the test of time and is still relevant and thought-provoking.",
    "name": "Classics"
    }
    ```
- **localhost:5000/api/genres/id**
  - ***DELETE*** - delete genre with specific id
  - ***PATCH*** - update genre with specific id, you can update all fields or some of them
    ```
    {
    "description": "When a book has stood the test of time and is still relevant and thought-provoking.",
    "name": "Classics"
    }
    ```
- **localhost:5000/api/authors**
  - ***GET*** - return all authors
  - ***POST*** - create new author
    ```
    {
    "birth_date": "1965-07-31",
    "name": "J. K. Rowling"
    }
    ```
- **localhost:5000/api/authors/id**
  - ***DELETE*** - delete authors with specific id
  - ***PATCH*** - update authors with specific id, you can update all fields or some of them
    ```
    {
    "birth_date": "1965-07-31",
    "name": "J. K. Rowling"
    }    
    ```
- **localhost:5000/api/books**
  - ***GET*** - return all books
  - ***POST*** - create new book
    ```
    {
    "author_id": 1,
    "description": "Most reviews were very favourable, commenting on Rowling's imagination, humour, simple, direct style and
    clever plot construction, although a few complained that the final chapters seemed rushed. ",
    "genre_id": 4,
    "name": "Harry Potter and the Philosopher's Stone",
    "price": 340.0,
    "publish_date": "1997-06-26",
    "rating": 8.7
    }
    ```
- **localhost:5000/api/books/id**
  - ***DELETE*** - delete books with specific id
  - ***PATCH*** - update books with specific id, you can update all fields or some of them
    ```
    {
    "author_id": 1,
    "description": "Most reviews were very favourable, commenting on Rowling's imagination, humour, simple, direct style and
    clever plot construction, although a few complained that the final chapters seemed rushed. ",
    "genre_id": 4,
    "name": "Harry Potter and the Philosopher's Stone",
    "price": 340.0,
    "publish_date": "1997-06-26",
    "rating": 8.7
    }
    ```
 




