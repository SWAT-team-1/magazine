from magazine.movies_bot import *

def test_cinemas_details():
    url = 'https://www.tajcinemas.com/'
    assert list == type(cinemas_details(url))

def test_upcoming_movies():
    assert None == upcoming_movies()






# def test_movies_by_year_and_genre(self):
#     self.type_of_movie = "Drama"
#     self.year_of_movie = 2000
#     actual = movies_by_year_and_genre(self.type_of_movie,self.year_of_movie)
#     expeected = None
#     assert actual == expeected