animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Write your code here
animal_movies_temp = list(animal_movies)

animal_movies_temp.append("Dumbo")
animal_movies_temp.append("Zootopia")

animal_movies = tuple(animal_movies_temp)

print("Updated animal movies:", animal_movies)