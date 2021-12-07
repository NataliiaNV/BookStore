"""
This module defines is used to populate database BookStore,
"""
from datetime import date

from bookstore_app.models.book_model import Book
from bookstore_app.models.genre_model import Genre
from bookstore_app.models.author_model import Author

from bookstore_app import db


def populate_database():
    """
    Populate database with genre
    :return: None
    """
    genre_1 = Genre(name='Classics', description='When a book has stood the test of time and is still relevant and thought-provoking.')
    genre_2 = Genre(name='Romance', description='Book where the main character or characters fall in love.'
                               'This category has so many different sub-categories.')
    genre_3 = Genre(name='Horror', description='Elements create fear for both the main character and the reader.')
    genre_4 = Genre(name='Fantasy', description='Fantasy books are set in an entirely fictional world, or a natural '
                                                'world with magical elements .')

    author_1 = Author(name='J. K. Rowling', birth_date=date(1965, 7, 31))
    author_2 = Author(name='F. Scott Fitzgerald', birth_date=date(1896, 9, 24))
    author_3 = Author(name='Jane Austen', birth_date=date(1775, 12, 16))
    author_4 = Author(name='Brenda Jackson')

    book_1 = Book(name='Harry Potter and the Philosopher\'s Stone', author_id=1, genre_id=4,
                  publish_date=date(1997, 6, 26),
                  description="Most reviews were very favourable, commenting on Rowling's imagination,"
                              " humour, simple, direct style and clever plot construction, although "
                              "a few complained that the final chapters seemed rushed. ", price=340, rating=8.7 )

    book_2 = Book(name='Harry Potter and the Chamber of Secrets', author_id=1, genre_id=4,
                  publish_date=date(1998, 7, 2),
                  description="Ever since Harry Potter had come home for the summer, the Dursleys had been so mean and "
                              "hideous that all Harry wanted was to get back to the Hogwarts School for Witchcraft and "
                              "Wizardry. But just as he's packing his bags, Harry receives a warning from a strange,"
                              " impish creature who says that if Harry returns to Hogwarts, disaster will strike.",
                  price=400, rating=9.2)

    book_3 = Book(name='Harry Potter and the Prisoner of Azkaban', author_id=1, genre_id=4,
                  publish_date=date(1999, 7, 8),
                  description="Thirteen-year-old Harry Potter spends another unhappy summer at the Dursleys. After Aunt"
                              " Marge insults Harry and his deceased parents, an angry Harry accidentally inflates her."
                              "Fearing expulsion from Hogwarts, he runs away. On a dark street, a"
                              " large black dog watches Harry.",
                  price=415, rating=7.9)

    book_4 = Book(name='The Great Gatsby', author_id=2, genre_id=1, publish_date=date(1925, 4, 10),
                  description="During World War II, the novel experienced an abrupt surge in popularity"
                              " when the Council on Books in Wartime distributed free copies to American "
                              "soldiers serving overseas. This new-found popularity launched a critical "
                              "and scholarly re-examination, and the work soon became a core part of most"
                              " American high school curricula and a part of American popular culture. ",
                  price=470.80, rating=8.5)

    book_5 = Book(name='Pride and Prejudice', author_id=3, genre_id=2, publish_date=date(1813, 1, 28),
                  description="Pride and Prejudice has consistently appeared near the top of lists of "
                              "most-loved books among literary scholars and the reading public. It has "
                              "become one of the most popular novels in English literature, with over 20 "
                              "million copies sold, and has inspired many derivatives in modern literature",
                  price=550, rating=9.3)

    book_6 = Book(name='Delaney’s Desert Sheikh', author_id=4, genre_id=2, publish_date=date(2002, 2, 1),
                  description="After graduating medical school, Delaney sets off for an escape at her "
                              "cousin's luxurious secluded cabin. But it turns out she's not staying "
                              "there alone, as it's also occupied by a gorgeous stranger named Jamal—who "
                              "also happens to be a sheikh determined to seduce Delaney.",
                  price=320.85, rating=7.8)

    book_1.genres = [book_1]
    book_1.authors = [book_1]
    book_2.genres = [book_2]
    book_2.authors = [book_2]
    book_3.genres = [book_3]
    book_3.authors = [book_3]
    book_4.genres = [book_4]
    book_4.authors = [book_4]
    book_5.genres = [book_5]
    book_5.authors = [book_5]
    book_6.genres = [book_6]
    book_6.authors = [book_6]

    db.session.add(genre_1)
    db.session.add(genre_2)
    db.session.add(genre_3)
    db.session.add(genre_4)

    db.session.add(author_1)
    db.session.add(author_2)
    db.session.add(author_3)
    db.session.add(author_4)

    db.session.add(book_1)
    db.session.add(book_2)
    db.session.add(book_3)
    db.session.add(book_4)
    db.session.add(book_5)
    db.session.add(book_6)

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    print('Clean database...')
    db.session.query(Genre).delete()
    db.session.query(Author).delete()
    db.session.query(Book).delete()
    print('Populating database...')
    populate_database()
    print('Successfully populated!')
