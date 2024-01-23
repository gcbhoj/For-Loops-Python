fav_movies = [1,5,7,3,1,1,5]

print(len(fav_movies))

fav_movies.append(10)
print(len(fav_movies))
print(fav_movies)
fav_movies.insert(1,25)
print(fav_movies)
del(fav_movies[2])
print(fav_movies)

for movies in fav_movies:
    print(movies)

fav_movies.sort()

print(fav_movies)


