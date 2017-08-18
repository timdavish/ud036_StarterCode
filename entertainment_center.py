import fresh_tomatoes
from media import Movie

# Create our movies
toy_story = Movie('Toy Story',
                  'A story of a boy and his toys that come to life',
                  'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                  'https://www.youtube.com/watch?v=vwyZH85NQC4')
avatar = Movie('Avatar',
               'A marine on an alien planet',
               'http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg',
               'https://www.youtube.com/watch?v=-9ceBgWV8io')
war_of_the_worlds = Movie('War of the Worlds',
                  'A dock worker struggles to protect his children from extraterrstrial war machines',
                  'https://upload.wikimedia.org/wikipedia/en/8/83/War_of_the_Worlds_2005_poster.jpg',
                  'https://www.youtube.com/watch?v=MJYnHA2OzfA')
shawshank_redepmtion = Movie('Shawshank Redemption',
               'A man sentenced to two life sentences in a tough prison for a crime he didn\'t commit is forced to take matters into his own hands',
               'https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg',
               'https://www.youtube.com/watch?v=6hB3S9bIaco')

# Store our movies in a list
movies = [toy_story, avatar, war_of_the_worlds, shawshank_redepmtion]

# Use the fresh_tomatoes module to open our movies page
fresh_tomatoes.open_movies_page(movies)

