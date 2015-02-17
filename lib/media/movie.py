__author__ = 'Luiz Arantes Sa'
from lib.media.video import Video


class Movie(Video):
    """
    Creates a Movie class from a json object.

    A movie json object must contain the following properties
      title - movie title
      duration - length of movie
      description - a brief description of the movie
      poster_image - movie cover url
      youtube_trailer - youtube trailer url
      genre - movie genre... Use pipeline separator for multiple
              genres for example, Action | Animation | Adventure
      movie_rating - eg. PG-13, R
      rating - review rating from 0-5
      year - year released

    Example below:
    {
      "title": "WALL-E",
      "duration": "98min",
      "description": "",
      "poster_image": "http://somesite.com/image.jpg",
      "youtube_trailer": "https://www.youtube.com/watch?v=FAfR8omt-CY",
      "genre": "Animation | Adventure | Romance",
      "movie_rating": "G",
      "rating": "4.5",
      "year": "2008"
    }
    """
    def __init__(self, json_movie):
        Video.__init__(self, json_movie['title'], json_movie['duration'], json_movie['description'])
        self.poster_image_url = json_movie['poster_image']
        self.trailer_youtube_url = json_movie['youtube_trailer']
        self.genre = json_movie['genre']
        self.rating = json_movie['rating']
        self.movie_rating = json_movie['movie_rating']
        self.year_released = json_movie['year']