
/**
 * Created by Luiz Arantes Sa on 2/15/15.
 */

$(function() {
    'use strict';

    /**
     * Creates a movie object from the given movie tile
     * @param movieTile {HTMLHtmlElement} movie tile
     * @constructor
     */
    var Movie = function (movieTile) {
        this.title = movieTile.find('h2').html();
        this.description = movieTile.find('.description').html();
        this.genre = movieTile.find('.genre').html();
        this.duration = movieTile.find('.duration').html();
        this.rating = movieTile.find('.rating').html();
        this.movieRating = movieTile.find('.movie-rating').html();
        this.src = movieTile.find('.tile-cover').attr('src');
        this.youtubeId = movieTile.find('.option-buttons').attr('data-trailer-youtube-id');
    };

    /**
     * Appends the given movie to `#modal-movie-info`
     * @param movie {Movie}
     */
    var appendToModalMovieInfo = function (movie) {
        var infoModal = $('#modal-movie-info');
        infoModal.data('movie', movie);
        infoModal.find('h2').html(movie.title);
        infoModal.find('.description').html(movie.description);
        infoModal.find('.genre').html(movie.genre);
        infoModal.find('.duration').html(movie.duration);
        infoModal.find('.rating').html(movie.rating);
        infoModal.find('.movie-rating').html(movie.movieRating);
        infoModal.find('.cover').attr('src',movie.src);
        infoModal.find('.play-trailer').attr('data-trailer-youtube-id',movie.youtubeId);
    };

    /**
     * Centers modal on page.
     * Snippet taken from: http://www.minimit.com/demos/vertical-center-bootstrap-3-modals
     */
    var centerModals = function () {
        $('.modal').each(function () {
            var $clone = $(this).clone().css('display', 'block').appendTo('body');
            var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
            top = top > 0 ? top : 0;
            $clone.remove();
            $(this).find('.modal-content').css("margin-top", top);
        });
    };

    /**
     * Displays a youtube video from the given youtube id.
     * @param youtubeId - Video ID used to embed youtube video
     */
    var showTrailer = function (youtubeId) {
        var sourceUrl = 'http://www.youtube.com/embed/' + youtubeId + '?autoplay=1&html5=1';
        $('#trailer-container').empty().append($("<iframe></iframe>", {
            'id': 'trailer-video',
            'type': 'text-html',
            'src': sourceUrl,
            'allowfullscreen': 'true',
            'frameborder': 0
        }));
        $('#modal-trailer').modal('show');
    };



    // Assure the modal is center on page by calling `centerModals()`
    // on window resize and when a modal shown.
    $('.modal').on('show.bs.modal', centerModals);
    $(window).on('resize', centerModals);

    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $('#modal-trailer').on('hide.bs.modal', function () {
        $("#trailer-container").empty();
    });

    // Set a listener for when the user clicks
    // on the "more info" button.
    $('.more-info').click(function () {
        // Get the movie tile from the clicked button
        var movieTile = $(this).parent().parent();
        // Create a movie object and properly attach it to `#modal-movie-info`
        var movie = new Movie(movieTile);
        appendToModalMovieInfo(movie);

        // Display movie info
        $('#modal-movie-info').modal('show');

    });

    var tiles = $('.tile-container');

    // Animate in the movies when the page loads
    tiles.hide().first().show("fast", function showNext() {
        $(this).next("div").show("fast", showNext);
    });

    // Play trailer when users clicks "play trailer"
    // button that is INSIDE a movie tile.
    tiles.find('.play-trailer').on('click', function () {
        var youtubeId = $(this).parent().attr('data-trailer-youtube-id');
        showTrailer(youtubeId);
    });

    // Play trailer when user clicks "play trailer"
    // button that is INSIDE `#modal-movie-info`
    $('#modal-movie-info').find('.play-trailer').click(function () {
        var infoModal = $('#modal-movie-info');
        infoModal.modal('hide');
        var movie = infoModal.data('movie');
        showTrailer(movie.youtubeId);
    });

    // Popup the movie cover in a modal when clicked.
    tiles.find('img').on('click', function () {
        var modalMovieCover = $('#modal-movie-cover');

        // Get the image from the tile and append it to the modal
        var image = $(modalMovieCover.find('.cover'));
        image.attr('src', $(this).attr('src'));

        // Create a copy of the image and append it to body to calculate picture width
        var clone = image.clone().css('display', 'block').appendTo('body');
        // Set the modal's width equal to the image
        modalMovieCover.find('.modal-dialog').css('width', clone.width());
        clone.remove(); // Remove the cloned image
        modalMovieCover.modal('show');
    });

    $('.rating').raty({
        readOnly: true,
        noRatedMsg : "This movie has no rating!",
        hints: ["Don't bother watching it...", 'Almost decent', 'Decent', 'Pretty good', 'Must watch!'],
        score: function() {
            return $(this).attr('data-score');
        }
    });

});
