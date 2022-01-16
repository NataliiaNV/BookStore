# BookStore
## Flask project simple web application

This project was created as the first step of an online bookstore to manage books and their authors, genres through a web application or with a help of REST API. It reads and writes data to a MySQL database. With this program you can:

- create, update and delete books, authors and genres
- search for books published between two dates or a specific date
- search for books by genre, author, or title
- calculate the average rating of authors based on the rating of their books

## Structure

forms - this package includes modules with forms for html templates
models - this package includes modules with Python classes describing DB models
rest - this package includes modules with REST API implementation
service - this package includes modules with functions to work with DB  
templates - html templates
controllers - this package include modules with Web controllers 
tests - this package includes modules with unit and integration tests
views - this package includes modules views

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
