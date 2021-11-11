import requests
from bs4 import BeautifulSoup 
import colorama 
colorama.init()
from colorama import Fore, Style
import datetime

url = "https://www.tajcinemas.com/"

genres = ["Drama","Action","Comedy","Fantasy","Horror","Mystery","Romance","Thriller"]
def cinemas_details(url):
    """
    function to get title, type, description and time for movie
    """ 

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
        all_data.append(f"{Fore.YELLOW}   ******************************************************************{i+1}********************************************************      {Style.RESET_ALL}")
        all_data.append("\U0001F3A5:"+movie_titles[i].text)
        all_data.append("\U0001F534:"+movie_types[i].text)
        all_data.append("\U0001F4DD:"+movie_descriptions[i].text.strip())
        times = [time.text for time in movie_times[i].find_all("span", {"class": "time"})]
        all_data.append(f'\U0001F55B:' +', '.join(times))
        all_data.append("\U0000231B:"+running_times[i].text.strip())

    for i in range(len(all_data)):
        print(all_data[i])
        print(" ")

    return all_data

# cinemas_details(url)





def movie_by_gen(user_name='User'):
    """
    function to get movie by genre
    """
    print(Fore.GREEN + 'Bot: What kind of movie do you want?:\U0001F50D' + Style.RESET_ALL)
    print(Fore.BLUE + f'{user_name}: ' + Style.RESET_ALL,end="")
    type_of = input().capitalize() 
    while not type_of.strip() in genres:
        print(Fore.GREEN + 'Bot: Please, enter the kind of movie do you want?:\U0001F50D' + Style.RESET_ALL)
        print(Fore.BLUE + f'{user_name}: ' + Style.RESET_ALL,end="")
        type_of = input().capitalize() 
    url = f"https://data-imdb1.p.rapidapi.com/movie/byGen/{type_of}/"

    querystring = {"page_size":"50"}
    headers = {
        'x-rapidapi-host': "data-imdb1.p.rapidapi.com",
        'x-rapidapi-key': "8fad0d25bfmshae608c562bfbf7dp196040jsn9a3c05b17e1a"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    gen_list = []
    print(f"{Fore.YELLOW}****************************************")
    print(f"********List of {type_of} movies \U0001F3A5 :******")
    print(f"*****************************************{Style.RESET_ALL}")
    print(" ")
    for i in range (10):
        gen_list.append (data['results'][i]['title'])
        print(f'{i+1}-'+gen_list[i])
        print("--------------------------")
    return gen_list

# movie_by_gen()



def upcoming_movies():
    """
    function to get upcoming movies
    """ 
    url = "https://data-imdb1.p.rapidapi.com/movie/order/upcoming/"
    querystring = {"page_size":"50"}
    headers = {
        'x-rapidapi-host': "data-imdb1.p.rapidapi.com",
        'x-rapidapi-key': "8fad0d25bfmshae608c562bfbf7dp196040jsn9a3c05b17e1a"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    print(f"{Fore.YELLOW}****************************************")
    print(f"********List of Upcoming Movies \U0001F3A5 :****")
    print(f"***************************************** {Style.RESET_ALL}")
    print(" ")
    for i in range (10):
      upcoming_name = data['results'][i]['title']
      upcoming_date = data['results'][i]['release']
      print(f'Release Date for "{upcoming_name}" is {upcoming_date}')
      print("----------------------------------------------------------")
    # return upcoming_name,upcoming_date
# upcoming_movies()




def rating_movie():
    """
    function to get rating for movies
    """ 
    url = "https://data-imdb1.p.rapidapi.com/movie/order/byRating/"
    querystring = {"page_size":"50"}
    headers = {
        'x-rapidapi-host': "data-imdb1.p.rapidapi.com",
        'x-rapidapi-key': "8fad0d25bfmshae608c562bfbf7dp196040jsn9a3c05b17e1a"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    print(" ")
    print(f"{Fore.YELLOW}****************************************")
    print(f"********List of Upcoming Movies \U0001F3A5 :****")
    print(f"*****************************************{Style.RESET_ALL}")
    print(" ")
    for i in range (10):
        movie_name= (data['results'][i]['title'])
        movie_rate = ( data['results'][i]['rating'])
        print(f'\U00002B50{movie_name} movie Rating is {movie_rate}')
        print("------------------------------------------------------")
    return movie_name,movie_rate
# rating_movie()




def movies_by_year_and_genre(user_name='User'):
    """
    function to get movie by genre
    """ 
    print(Fore.GREEN + 'Bot: What kind of movie do you want?:\U0001F50D' + Style.RESET_ALL)
    print(Fore.BLUE + f'{user_name}: ' + Style.RESET_ALL,end="")
    type_of_movie = input().capitalize()
    while not type_of_movie.strip() in genres:
        print(Fore.GREEN + 'Bot: Please, enter the kind of movie do you want?:\U0001F50D' + Style.RESET_ALL)
        print(Fore.BLUE + f'{user_name}: ' + Style.RESET_ALL,end="")
        type_of_movie = input().capitalize() 
    print(Fore.GREEN + 'Bot: What year are you looking for?\U0001F50D' + Style.RESET_ALL)
    print(Fore.BLUE + f'{user_name}: ' + Style.RESET_ALL,end="")
    year_of_movie = input()
    x = datetime.datetime.now()
    date = x.strftime('%Y')
    year_list = [f'{year}' for year in range(1960,int(date)+1)]
    while not year_of_movie.strip() in year_list:
        print(Fore.GREEN + 'Bot: Please, enter the year are you looking for?\U0001F50D' + Style.RESET_ALL)
        print(Fore.BLUE + f'{user_name}: ' + Style.RESET_ALL,end="")
        year_of_movie = input()

    url = f"https://data-imdb1.p.rapidapi.com/movie/byYear/{year_of_movie}/byGen/{type_of_movie}/"
    querystring = {"page_size":"50"}
    headers = {
        'x-rapidapi-host': "data-imdb1.p.rapidapi.com",
        'x-rapidapi-key': "8fad0d25bfmshae608c562bfbf7dp196040jsn9a3c05b17e1a"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    print(" ")
    print(f"{Fore.YELLOW}*******************************")
    print(f'*List of {type_of_movie} movie in {year_of_movie}\U0001F3A5*')
    print(f"*******************************{Style.RESET_ALL}")
    print(" ")
    for i in range (10):
        year_and_genre = (data['results'][i]['title'])
        print(f'{year_and_genre}')
        print("------------------------")
    return year_and_genre

# movies_by_year_and_genre()


def all_movie_function(user_name='User'):
    """
    function to collect all functions
    """ 
    user_input = None
    while user_input != 'q':

        print('''   
                \U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5
                \U0001F4A5\U0001F4A5\U0001F3A5Movie Section \U0001F3A5\U0001F4A5\U0001F4A5
                \U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5''')
 
        print(f'''
\U0001F3A5 If you want to know the movies available in the cinema, write (1)
\U0001F3A5 If you want to search for films by genre, write (2)
\U0001F3A5 If you want to search for upcoming  movies, write (3)
\U0001F3A5 If you want to search for movies rating , write(4) 
\U0001F3A5 if you want to search for by genre and year, write(5)
''')

        print(Fore.GREEN + 'Bot: Choose from the list or (q) to quit' + Style.RESET_ALL)
        print(Fore.BLUE + f'{user_name}: ' + Style.RESET_ALL,end="")
        user_input = input()  
        if user_input == "1":
            cinemas_details(url)
            print(Fore.GREEN + 'Bot: Write (q)uit or (b)ack to list' + Style.RESET_ALL)
            print(Fore.BLUE + f'{user_name}: ' + Style.RESET_ALL,end="")
            user_input = input()  
            if user_input == 'b':
                continue

        elif user_input == "2":
            movie_by_gen(user_name)
            print(Fore.GREEN + 'Bot: Write (q)uit or (b)ack to list' + Style.RESET_ALL)
            print(Fore.BLUE + f'{user_name}: ' + Style.RESET_ALL,end="")
            user_input = input()  
            if user_input == 'b':
                continue

        elif user_input == "3":
            upcoming_movies()
            print(Fore.GREEN + 'Bot: Write (q)uit or (b)ack to list' + Style.RESET_ALL)
            print(Fore.BLUE + f'{user_name}: ' + Style.RESET_ALL,end="")
            user_input = input()  
            if user_input == 'b':
                continue


        elif user_input == "4":
            rating_movie()
            print(Fore.GREEN + 'Bot: Write (q)uit or (b)ack to list' + Style.RESET_ALL)
            print(Fore.BLUE + f'{user_name}: ' + Style.RESET_ALL,end="")
            user_input = input()  
            if user_input == 'b':
                continue

        elif user_input == "5":
            movies_by_year_and_genre(user_name)
            print(Fore.GREEN + 'Bot: Write (q)uit or (b)ack to list' + Style.RESET_ALL)
            print(Fore.BLUE + f'{user_name}: ' + Style.RESET_ALL,end="")
            user_input = input()  
            if user_input == 'b':
                continue

        if user_input == 'q':
            break
        else :
            continue
            # user_input = input(f'''
            # please Chose from list:*****************************************
            # or q for quit
            # (1) for cinemas details
            # (2) for movie_by_gen
            # (3) for upcoming_movies
            # (4) for rating_movie
            # (5) for movies_by_year_and_genre

            # ''')


if __name__ == '__main__':
    all_movie_function()
