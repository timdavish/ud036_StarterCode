import webbrowser

class Video():
    """
    This class provides a way to store basic video properties
    """

    def __init__(self, title, trailer_youtube_url):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        print('called')
        webbrowser.open(self.trailer_youtube_url)

class Movie(Video):
    """
    This class provides a way to store movie related information
    """
    
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        Video.__init__(self, title, trailer_youtube_url)
        
        self.storyline = storyline
        self.poster_image_url = poster_image_url

    def show_trailer(self):
        Video.show_trailer(self)
