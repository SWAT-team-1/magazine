from magazine.movies_bot import movie_by_gen,cinemas_details,movies_by_year_and_genre,upcoming_movies, rating_movie,upcoming_movies
import mock
import builtins

from magazine.stock_market_bot import get_daily_stock_exchange

def test_cinemas_details():
    url = 'https://www.tajcinemas.com/'
    assert list == type(cinemas_details(url))

def test_upcoming_movies():
    assert None == upcoming_movies()


def test_movie_rate():
    assert ('Pulp Fiction', 8.9) == rating_movie()

def test_movie_by_gen():
    expected = 'Thunder Force'
    with mock.patch('builtins.input',return_value = 'action'):
        assert movie_by_gen()[0] == expected
    