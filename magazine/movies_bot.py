from os import times
import requests
from bs4 import BeautifulSoup 
import emoji

# from itertools import zip_longest
# import csv
url = "https://www.tajcinemas.com/"
def cinemas_details(url):
    """
    function to get title, type, description and time for movie
    """ 
    # url = "https://www.tajcinemas.com/"
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup (src , 'html.parser')

    movie_titles = soup.find_all("h3", {"class": "no-underline"})
    movie_types = soup.find_all("span", {"class": "title"})
    movie_descriptions = soup.find_all("p", {"class": "synopsis"})
    running_times = soup.find_all("div", {"class": "col-md-4 col-sm-3 running-time"} )
    movie_times = soup.find_all("div", {"class": "col-md-8 col-sm-9"})    

    
    all_data = []
    for i in range(len(movie_titles)-4):
        all_data.append(f"**************************************************{i+1}*********************************************************")
        all_data.append("-Movie name :"+movie_titles[i].text)
        all_data.append("-Movie type: "+movie_types[i].text)
        all_data.append("-Description of movie: "+movie_descriptions[i].text.strip())
        times = [time.text for time in movie_times[i].find_all("span", {"class": "time"})]
        all_data.append(f'-Viewing times:' +', '.join(times))
        all_data.append("-Running time: "+running_times[i].text.strip())

    for i in range(len(all_data)):
        print(all_data[i])

    return all_data

########################################################################################################
    # file_list = [Movie_title , Movie_type, Movie_description , Movie_time]
    # exported = zip_longest(*file_list)
    # with open("test1.csv", 'w') as file:
    #     wr= csv.writer(file)
    #     wr.writerow(["Movie_title", "Movie_type", "Movie_description" ," Movie_time"])
    #     wr.writerows(exported)

    # return Movie_title , Movie_type , Movie_description , Movie_time
########################################################################################################

# cinemas_details(url)



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
    gen_list = []
    print(f"List of {type_of} movies :")
    print(" ")
    for i in range (10):
        gen_list.append (data['results'][i]['title'])
        print(f'{i+1}-'+gen_list[i])
        print("--------------------------")
    # return gen_list
# movie_by_gen()



def upcoming_movies():
    url = "https://data-imdb1.p.rapidapi.com/movie/order/upcoming/"
    querystring = {"page_size":"50"}
    headers = {
        'x-rapidapi-host': "data-imdb1.p.rapidapi.com",
        'x-rapidapi-key': "8fad0d25bfmshae608c562bfbf7dp196040jsn9a3c05b17e1a"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    
    # upcoming_name = []
    # upcoming_date = []
    for i in range (10):
      print("-----------------------------")
      upcoming_name = data['results'][i]['title']
      upcoming_date = data['results'][i]['release']
      print(f'Release Date for "{upcoming_name}" is {upcoming_date}')
    
# upcoming_movies()

def rating_movie():
    url = "https://data-imdb1.p.rapidapi.com/movie/order/byRating/"
    querystring = {"page_size":"50"}
    headers = {
        'x-rapidapi-host': "data-imdb1.p.rapidapi.com",
        'x-rapidapi-key': "8fad0d25bfmshae608c562bfbf7dp196040jsn9a3c05b17e1a"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()

    # rate_list = []
    for i in range (10):
        movie_name= (data['results'][i]['title'])
        movie_rate = ( data['results'][i]['rating'])
        print(f'\U00002B50{movie_name} movie Rating is {movie_rate}')
        print("---------------------------------------------")

# rating_movie()

def movies_by_year_and_genre(type_of_movie ,year_of_movie):
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
    print("              *******************************")
    print(f'              **List of {type_of_movie} movie in {year_of_movie}**')
    print("              *******************************")
    for i in range (10):
        year_and_genre = (data['results'][i]['title'])
        print(f'                        {year_and_genre}')
        # print("               -------------------------------------")
    return year_and_genre

# movies_by_year_and_genre()