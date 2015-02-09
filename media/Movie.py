__author__ = 'Luiz Arantes Sa'
from video import Video


class Movie(Video):

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, title, duration, description, poster_image, trailer_youtube_url):
        Video.__init__(self, title, duration, description)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url