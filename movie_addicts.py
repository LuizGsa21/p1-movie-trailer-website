__author__ = 'Luiz Arantes Sa'

import webbrowser
import os
import re


def create_movie_tiles_content(movies):
    """

    :param movies: lib.movie.media.Movie
    :return: movie
    """
    """
    :param movies:
    :return:
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
            description=movie.description
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


def get_header():
    header = open('templates/header.html', 'r').read()  # header file
    style = open('templates/style.css', 'r').read()  # style CSS

    # Insert the style into the header, then return header content
    return header.format(my_style=style)


def get_footer():
    # Get the footer content
    footer = open('templates/footer.html', 'r').read()  # footer file

    # Insert the app JavaScript, then return footer content
    return footer.format(my_app=open('templates/app.js', 'r').read())


def open_movies_page(movies):
    # Get header content with styles attached
    content = get_header()

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    content += create_movie_tiles_content(movies)

    # Add the finishing touch to content. aka footer
    content += get_footer()

    # Create or overwrite the output file
    output_file = open('movie_addicts.html', 'w')

    # Output the file
    output_file.write(content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible