# this creates a class with the initialize function
class Movie:
    # everytime that this class is called the function __init__ will run,
    # so remember to respect the order of the initialization: title,
    #  youtube_url, storyline and poster_image_url

    def __init__(self, name, youtube_url, storyline, film_photo):
        self.title = name
        self.trailer_youtube_url = youtube_url
        self.storyline = storyline
        self.poster_image_url = film_photo
