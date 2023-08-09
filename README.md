# Movie Recommendation Mashup

This Python project involves combining data from two different APIs to create movie recommendations. The TasteDive API provides related items based on a query input, while the OMDB API provides information about movies, including review scores. This code demonstrates the process of fetching, processing, and sorting movie data to generate recommended movies.

## Project Overview

The main objective of this project is to provide users with movie recommendations based on their input. The two APIs used are:

1. **TasteDive API:** This API allows you to provide a movie title as a query input and get back a set of related items, such as movies, bands, and TV shows.

2. **OMDB API:** The OMDB API enables you to retrieve data about a specific movie, including scores from various review sites like Rotten Tomatoes, IMDB, etc.

This is an application of mashing up these APIs to create a movie recommendation system. Here's a step-by-step breakdown of the process:

1. Fetch data from TasteDive to get related movies for a given list of titles.
2. Combine the resulting lists of related movies.
3. Sort the combined list of related movies based on their Rotten Tomatoes scores (this requires making API calls to the OMDB API).

## How to Use

1. **Fetch Data from TasteDive**: The `get_movies_from_tastedive` function takes a movie title as input and returns 5 TasteDive results associated with that title.

2. **Extract Movie Titles**: The `extract_movie_titles` function extracts the list of movie titles from a dictionary returned by the TasteDive API.

3. **Get Related Titles**: The `get_related_titles` function takes a list of movie titles and retrieves five related movies for each title. It then combines these related titles into a single list, removing duplicates.

4. **Fetch Data from OMDB**: The `get_movie_data` function fetches data about a movie using the OMDB API. Provide a movie title, and it will return a dictionary with information about that movie.

5. **Get Movie Rating**: The `get_movie_rating` function extracts the Rotten Tomatoes rating from an OMDB dictionary result for a movie. If there's no Rotten Tomatoes rating, it returns 0.

6. **Get Sorted Recommendations**: The `get_sorted_recommendations` function takes a list of movie titles and returns a sorted list of related movie titles. The sorting is based on the Rotten Tomatoes ratings of the related movies.

## Code Example

```python
# Use the provided functions to get movie recommendations
recommended_movies = get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
for movie in recommended_movies:
    print(movie)
```

This will output a list of movie titles recommended based on the input titles "Bridesmaids" and "Sherlock Holmes," sorted by their Rotten Tomatoes ratings.

## Additional Notes

Make sure you have the required libraries installed. You can install them using the following:

```bash
pip install requests
```

To run the code, simply copy and paste it into a Python file and execute it. You can customize the input movie titles in the `get_sorted_recommendations` function to get recommendations based on your preferences.

Enjoy exploring and discovering new movies with this recommendation mashup project!