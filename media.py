import webbrowser

# Parent class for any type of Video
class Video():
    """
    This class provides a way to store basic video properties
    """

    # Video constructor
    def __init__(self, title, trailer_youtube_url):
        self.title = title
        self.trailer_youtube_url = trailer_youtube_url

    # Opens the video's trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

# Movie class which extends Video just for practice.
# This is not necessary in this project because we don't have any other types
# of Videos, but helped me learn inheritence syntax in python.
class Movie(Video):
    """
    This class provides a way to store movie related information
    """
    
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    # Movie constructor
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        Video.__init__(self, title, trailer_youtube_url)
        
        self.storyline = storyline
        self.poster_image_url = poster_image_url

