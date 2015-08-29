"""The following code defines some instances of the class Movie()"""
import media
import fresh_tomatoes

barry_lyndon = media.Movie(
	"Barry Lyndon",
	"An Irish rogue wins the heart of a rich widow and assumes her dead \
    husband's aristocratic position in 18th-century England.",
    "https://homoclassicus.files.wordpress.com/2013/08/barry-lyndon-poster.jpg?w=868",  # noqa
    "https://www.youtube.com/watch?v=dZGPy4C2XVw"
)

interstellar = media.Movie(
    "Interstellar",
    "A team of explorers travel through a wormhole in space in an attempt \
    to ensure humanity's survival.",
    "https://d3ui957tjb5bqd.cloudfront.net/uploads/2014/11/interstellar-poster-3.png",  # noqa
    "https://www.youtube.com/watch?v=2LqzF5WauAw"
)

ex_machina = media.Movie(
    "Ex Machina",
    "A young programmer is selected to participate in a ground-breaking \
    experiment in artificial intelligence by evaluating the human \
    qualities of a breath-taking female A.I.",
    "http://www.joblo.com/posters/images/full/ex-machina-poster.jpg",
    "https://www.youtube.com/watch?v=sNExF5WYMaA"
)

demolition_man = media.Movie(
    "Demolition Man",
    "A police officer is brought out of suspended animation in prison to \
    pursue an old ultra-violent nemesis who is loose in a non-violent \
    future society.",
    "http://www.reviewstl.com/wp-content/uploads/2010/04/Demolition-Man-Movie-Poster-Stallone-Snipes.jpg",  # noqa
    "https://www.youtube.com/watch?v=ViwrF2Y4nX8"
)

cloud_atlas = media.Movie(
    "Cloud Atlas",
    "An exploration of how the actions of individual lives impact one \
    another in the past, present and future, as one soul is shaped from a \
    killer into a hero, and an act of kindness ripples across centuries to \
    inspire a revolution.",
    "http://www.joblo.com/posters/images/full/cloud-atlas-final-poster.jpg",
    "https://www.youtube.com/watch?v=ByehYal_cCs"
)

the_matrix = media.Movie(
    "The Matrix",
    "A computer hacker learns from mysterious rebels about the true nature \
    of his reality and his role in the war against its controllers.",
    "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1__SX1217_SY857_.jpg",  # noqa
    "https://www.youtube.com/watch?v=m8e-FF8MsqU"
)

# List the class instances so that they can be easily passsed to the
# website building function
movies = [
    barry_lyndon,
    interstellar,
    ex_machina,
    demolition_man,
    cloud_atlas,
    the_matrix
]

# Call the website building function to get to work on the list movies
fresh_tomatoes.open_movies_page(movies)

