# Modules
import os
import csv

# # Prompt user for video lookup
# video = input("What show or movie are you looking for? ")

# Set path for file
file_to_load = os.path.join('..',"Resources", "netflix_ratings.csv")
file_to_save = os.path.join("analysis", "netflix_ratings.txt")


# Open the CSV

with open(file_to_load, "r") as movie_data :
    file_reader = csv.reader(movie_data)
  
    for row in file_reader:
        print(row)

        