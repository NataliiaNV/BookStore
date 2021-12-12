from bookstore_app.models.genre_model import Genre


class GenresService:

    @classmethod
    def get_genres(cls):
        return Genre.query.order_by(Genre.id)
