__author__ = 'Luiz Arantes Sa'
import json
import movie_addicts
from lib.media import movie

# Get the movie collection from movies.json
json_data = open('movies.json', 'r')
movies = json.loads(json_data.read())

all_movies = []
# Create Movie objects from the json content
# and append it to `all_movies`
for current_movie in movies:
    all_movies.append(movie.Movie(json_movie=current_movie))

# Create the movies page using `all_movies`
movie_addicts.open_movies_page(all_movies)