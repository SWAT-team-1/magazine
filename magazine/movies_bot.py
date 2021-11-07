import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
import csv


def cinemas_details():
    """
    function to get title, type, description and time for movie
    """ 
    url = "https://www.tajcinemas.com/"
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup (src , 'html.parser')

    Movie_titles = soup.find_all("h3", {"class": "no-underline"})
    Movie_types = soup.find_all("span", {"class": "title"})
    Movie_descriptions = soup.find_all("p", {"class": "synopsis"})
    Movie_times = soup.find_all("span", {"class": "time"})

    Movie_title = []
    Movie_type = []
    Movie_description = []
    Movie_time = []

    for i in range(len(Movie_titles)):
        Movie_title.append(Movie_titles[i].text)
        Movie_type.append(Movie_types[i].text)
        Movie_description.append(Movie_descriptions[i].text)
        Movie_time.append(Movie_times[i].text)

    file_list = [Movie_title , Movie_type, Movie_description , Movie_time]
    exported = zip_longest(*file_list)
    with open("test1.csv", 'w') as file:
        wr= csv.writer(file)
        wr.writerow(["Movie_title", "Movie_type", "Movie_description" ," Movie_time"])
        wr.writerows(exported)

    return Movie_title , Movie_type , Movie_description , Movie_time


# print(cinemas_details())



def movie_by_gen():
    type_of = input("What kind of movie do you want?: ")
    url = f"https://data-imdb1.p.rapidapi.com/movie/byGen/{type_of}/"

    querystring = {"page_size":"50"}
    headers = {
        'x-rapidapi-host': "data-imdb1.p.rapidapi.com",
        'x-rapidapi-key': "8fad0d25bfmshae608c562bfbf7dp196040jsn9a3c05b17e1a"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()

    for i in range (10):
        print(data['results'][i]['title'])

# print(movie_by_gen())



def upcoming_movies():
    url = "https://data-imdb1.p.rapidapi.com/movie/order/upcoming/"
    querystring = {"page_size":"50"}
    headers = {
        'x-rapidapi-host': "data-imdb1.p.rapidapi.com",
        'x-rapidapi-key': "8fad0d25bfmshae608c562bfbf7dp196040jsn9a3c05b17e1a"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    
    upcoming = []
    for i in range (10):
        upcoming.append({data['results'][i]['title'] , data['results'][i]['release']})
    return upcoming

# print(upcoming_movies())

def rating_movie():
    url = "https://data-imdb1.p.rapidapi.com/movie/order/byRating/"
    querystring = {"page_size":"50"}
    headers = {
        'x-rapidapi-host': "data-imdb1.p.rapidapi.com",
        'x-rapidapi-key': "8fad0d25bfmshae608c562bfbf7dp196040jsn9a3c05b17e1a"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()

    rate_movie = []
    for i in range (10):
        rate_movie.append({data['results'][i]['title'] , data['results'][i]['rating']})
    return rate_movie

# print(rating_movie())



def movies_by_year_and_genre():
    type_of_movie = input("What kind of movie do you want?: ")
    year_of_movie = input("What year are you looking for?: ")

    url = f"https://data-imdb1.p.rapidapi.com/movie/byYear/{year_of_movie}/byGen/{type_of_movie}/"
    querystring = {"page_size":"50"}
    headers = {
        'x-rapidapi-host': "data-imdb1.p.rapidapi.com",
        'x-rapidapi-key': "8fad0d25bfmshae608c562bfbf7dp196040jsn9a3c05b17e1a"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    year_and_genre = []
    for i in range (10):
        year_and_genre.append(data['results'][i]['title'])
    return year_and_genre

# print(movies_by_year_and_genre())
