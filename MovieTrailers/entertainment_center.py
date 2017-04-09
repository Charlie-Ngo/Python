import media
import fresh_tomatoes


# This is an instance of the class
doctor_strange = media.Movie("Doctor Strange"
                             ,"The Origin of Doctor Steven Strange the Sorcerer Supreme"
                             ,"http://static.metacritic.com/images/products/movies/1/9973cbbacdf341aaf41efb33d68d7772.jpg"
                             ,"https://www.youtube.com/watch?v=HSzx-zryEgM"
                             )
guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy"
                                     ,"A group of misfits save the galaxy."
                                     ,"http://www.film-rezensionen.de/wp-content/uploads/2014/08/Guardians-of-the-Galaxy.jpg"
                                     ,"https://www.youtube.com/watch?v=d96cjJhvlMA"
                                     )

avengers = media.Movie("Avengers"
                      ,"Earth's Mightiest Heroes"
                      ,"https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg"
                      ,"https://www.youtube.com/embed/eOrNdBpGMv8"
                      )

princess_bride = media.Movie("Princess Bride"
                          ,"A satire of the classic hero movie"
                          ,"http://static.rogerebert.com/uploads/movie/movie_poster/the-princess-bride-1987/large_elDCZNBSZFHncpYThVdNM73c0P.jpg"
                          ,"https://www.youtube.com/watch?v=njZBYfNpWoE"
                           )

inception = media.Movie("Inception"
                       ,"A thief with the ability to enter people's dreams."
                       ,"http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-5.jpg"
                       ,"https://www.youtube.com/watch?v=YoHD9XEInc0"
                        )

hackers = media.Movie("Hackers"
                     ,"A teenage hacker finds himself framed for the theft of millions of dollars from a major corporation."
                     ,"https://images-na.ssl-images-amazon.com/images/M/MV5BODg0NjQ5ODQ3OF5BMl5BanBnXkFtZTcwNjU4MjkzNA@@._V1_UY1200_CR85,0,630,1200_AL_.jpg"
                     ,"https://www.youtube.com/watch?v=Rn2cf_wJ4f4"
                     )
# This is a list variable that will be passed as an argument
movies = [princess_bride,inception,hackers,doctor_strange,guardians_of_the_galaxy,avengers]
print(media.Movie.__module__)
#fresh_tomatoes.open_movies_page(movies)