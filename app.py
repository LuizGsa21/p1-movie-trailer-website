import fresh_tomatoes
from media import movie
import json

__author__ = 'Luiz Arantes Sa'

json_data = open('movies.json', 'r')
movies = json.loads(json_data.read())['movies']

all_movies = []
for myMovie in movies:
    all_movies.append(movie.Movie(myMovie['title'],
                                  myMovie['duration'],
                                  myMovie['description'],
                                  myMovie['poster_image'],
                                  myMovie['youtube_trailer']))
fresh_tomatoes.open_movies_page(all_movies)