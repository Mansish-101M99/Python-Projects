# pip install IMDbPY
import imdb

av = imdb.IMDb()
movie_nm = input("Enter the movie name : ")
movies = av.search_movie((str(movie_nm)))
index = movies[0].getID()

movie = av.get_movie(index)
movie_title = movie['title']
movie_year = movie['year']
movie_cast = movie['cast']
list_of_cast = ', '.join(map(str, movie_cast))

print("Title of the movie : ", movie_title)
print("Year of release for the movie : ", movie_year)
print("Cast of the movie : ", movie_cast)
