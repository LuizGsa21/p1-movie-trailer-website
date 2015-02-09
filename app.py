import fresh_tomatoes
import json
from media import movie

__author__ = 'Luiz Arantes Sa'

json_data = open('movies.json', 'r')
movies = json.loads(json_data.read())['movies']

all_movies = []
for current_movie in movies:
    all_movies.append(movie.Movie(current_movie['title'],
                                  current_movie['duration'],
                                  current_movie['description'],
                                  current_movie['poster_image'],
                                  current_movie['youtube_trailer']))
fresh_tomatoes.open_movies_page(all_movies)