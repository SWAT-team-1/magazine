from magazine.movies_bot import movie_by_gen,cinemas_details,upcoming_movies, rating_movie,upcoming_movies

def test_cinemas_details():
    url = 'https://www.tajcinemas.com/'
    assert list == type(cinemas_details(url))

def test_upcoming_movies():
    assert None == upcoming_movies()


def test_movie_rate():
    assert ('Pulp Fiction', 8.9) == rating_movie()