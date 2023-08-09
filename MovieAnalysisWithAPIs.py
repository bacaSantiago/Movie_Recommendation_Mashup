"""_summary_
This project will take you through the process of mashing up data from two different APIs to make movie recommendations. 
The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. 
The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).

You will put those two together. You will use TasteDive to get related movies for a whole list of titles. 
You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)
Your first task will be to fetch data from TasteDive. The documentation for the API is at https://tastedive.com/read/api.
"""

import requests
import json

# Dictionary to store cached responses
cache = {}

# Function to convert a dictionary to a hashable tuple
def hashable_dict(d):
    return tuple(sorted(d.items()))

# Function to make HTTP requests with caching
def make_request(endpoint, params):
    hashed_params = hashable_dict(params)
    
    if endpoint in cache and hashed_params in cache[endpoint]:
        print("Found in cache")
        return cache[endpoint][hashed_params]
    
    response = requests.get(endpoint, params=params)
    response_json = response.json()  # Parse the JSON response
    
    if endpoint not in cache:
        cache[endpoint] = {}
    cache[endpoint][hashed_params] = response_json
    
    return response_json


"""_get_movies_from_tastedive_
Function that takes one input parameter, a string that is the name of a movie or music artist. 
The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, 
not other kinds of media. 
It will be a python dictionary with just one key, 'Similar'.
"""
def get_movies_from_tastedive(title):
    endpoint = 'https://tastedive.com/api/similar'
    param = {}
    param['q']= title
    param['type']= 'movies'
    param['limit']= 5
    
    page_cache = make_request(endpoint, param)
    return json.loads(page_cache)


"""_extract_movie_titles_
Function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive
"""
def extract_movie_titles(dic):
    return ([i['Name'] for i in dic['Similar']['Results']])

tony_bennett = extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
print("\n  -  Similar movies to Tonny Bennett")
for i in tony_bennett:
    print(i)
    
    
"""_get_related_titles_
Function that takes a list of movie titles as input. It gets five related movies for each from TasteDive, 
extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.
"""
def get_related_titles(movie_list):
    relatedMovies = []
    for movie in movie_list:
        relatedMovies.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(relatedMovies)) # Set is a type of list, unordered, unchangeable, and without duplicates

print(get_related_titles(["Black Panther", "Captain Marvel"]))


"""_get_movie_data_
Function that fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/
Function that takes in one parameter which is a string that should represent the title of a movie you want to search.
The function should return a dictionary with information about that movie. 
"""
def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'
    
    page_cache = make_request(endpoint, param)
    return json.loads(page_cache)

print(get_movie_data("Venom"))
print(get_movie_data("Baby Mama"))

"""_get_movie_rating_
Function that takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. 
For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.
"""
def get_movie_rating(dic):
    ranking = dic['Ratings']
    for i in ranking:
        if i['Source'] == 'Rotten Tomatoes':
            return int(i['Value'][:-1])
    return 0

print("  -  Rotten Tomatoes rating for Deadpool 2")
print(get_movie_rating(get_movie_data("Deadpool 2")))


"""_get_sorted_recommendations_
Function that takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. 
The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function.
"""
def get_sorted_recommendations(movie_list):
    recommended_dict = {}
    for i in get_related_titles(movie_list):
        recommended_dict[i] = get_movie_rating(get_movie_data(i))
    sorted_movies = sorted(recommended_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)
    #return [i[0] for i in sorted(recommended_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]
    sorted_movie_titles = [movie[0] for movie in sorted_movies]
    return sorted_movie_titles

print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))