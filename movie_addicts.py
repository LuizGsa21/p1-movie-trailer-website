__author__ = 'Luiz Arantes Sa'

import webbrowser
import os
import re


def create_movie_tiles_content(movies):
    """
    Generates movie tiles from the movie list using
    "tile-container.html" as a template.

    :param movies:
    :type movies: list lib.media.movie
    :return: the generated movie tiles.
    :rtype: str
    """
    tile_template = open('templates/tile-container.html', 'r').read()
    content = ''
    # Keep track of the current movie tile
    # so we know when to insert a clearfix div
    count = 1
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
        # Append the tile for the movie with its contents filled in
        content += tile_template.format(
            title=movie.title,
            cover=movie.poster_image_url,
            youtube_id=trailer_youtube_id,
            score=movie.rating,
            genre=movie.genre,
            duration=movie.duration,
            movie_rating=movie.movie_rating,
            description=movie.description,
            year=movie.year_released
        )
        clearfix = ''
        if count % 2 == 0:  # Add small grid clearfix every 2 tiles
            clearfix += ' visible-sm-block '
        if count % 3 == 0:  # Add medium/large grid clearfix every 3 tiles
            clearfix += ' visible-md-block  visible-lg-block '
        if len(clearfix) > 0:  # append clearfix if needed
            content += '<div class="clearfix ' + clearfix + '"></div>'

        count += 1

    return content


def open_movies_page(movies):
    """
    Creates a web page from the list of movies and opens it using
    the default web browser.

    Note: Opens in a new tab if possible.

    :param movies: list of movies
    :type movies: list lib.media.movie
    :return: absolutely nothing ;)
    """
    # Get header content
    content = open('templates/header.html', 'r').read()

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    content += create_movie_tiles_content(movies)

    # Append the footer content
    content += open('templates/footer.html', 'r').read()

    # Create or overwrite the output file
    output_file = open('movie_addicts.html', 'w')

    # Output the file
    output_file.write(content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible