import fresh_tomatoes
from media import movie
import json

__author__ = 'Luiz Arantes Sa'

toy_story = movie.Movie('Toy Story',
                        '1h 30 min',
                        'A story of a boy and his toys that come to life.',
                        'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=vwyZH85NQC4')
avatar = movie.Movie('Avatar',
                     '1h 30 min',
                     'A marine on an alien planet',
                     'http:upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')
school_of_rock = movie.Movie('School of Rock',
                             '1h 30 min',
                             'A marine on an alien planet',
                             'http:upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
                             'https://www.youtube.com/watch?v=3PSUJFEBC74')
ratatouille = movie.Movie('Ratatouille',
                          '1h 30 min',
                          'A rat is a chef in Paris',
                          'http:upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
                          'https://www.youtube.com/watch?v=c3sBBRxDAqk')
midnight_in_paris = movie.Movie('Midnight in Paris',
                                '1h 30 min',
                                'Going back in time to meet authors',
                                'http:upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg',
                                'https://www.youtube.com/watch?v=FAfR8omt-CY')
hunger_games = movie.Movie('Hunger Games',
                           '1h 30 min',
                           'A really real reality show',
                           'http:upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg',
                           'https://www.youtube.com/watch?v=PbA63a7H0bo')

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

# fresh_tomatoes.open_movies_page(movies)
json_data = open('movies.json', 'r')
movies = json.loads(json_data.read())['movies']

for movie in movies:
    print movie['title']