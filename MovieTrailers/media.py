import webbrowser


class Movie():
    """ This class provides a way to store moving related information """
    # Class variable, based on Google style guide, the class variables should be in all uppercase
    VALID_RATINGS = ["G","PG","PG-13","R"]
    # This is the constructor
    def __init__(self,movie_title, movie_storyline, poster_image,trailer_youtube):
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube

    # This is an instance method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)