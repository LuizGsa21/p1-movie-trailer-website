__author__ = 'Luiz Arantes Sa'
from json import loads
import movie_addicts
from lib.media import movie

# Get the movie collection from movies.json
with open('movies.json', 'r') as json_data:
    movies = loads(json_data.read())

all_movies = []
# Create Movie objects from the json content
# and append it to `all_movies`
for current_movie in movies:
    all_movies.append(movie.Movie(json_movie=current_movie))

# Create the movies page using `all_movies`
movie_addicts.open_movies_page(all_movies)