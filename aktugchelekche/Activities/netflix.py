# Modules
import os
import csv
user_input = "y"
# # Prompt user for video lookup
while user_input == "y":
    video = input("What show or movie are you looking for? ")

    # Set path for file
    file_to_load = os.path.join("Resources1", "netflix_ratings.csv")


    # Open the CSV

    with open(file_to_load, "r") as movie_data :
        file_reader = csv.reader(movie_data)
        found = False
        for row in file_reader:  
            if video == row[0]:
                found= True
                print(f'{video} has rating of {row[5]}')
                break
        else:
            print("Not Found!")
            

        user_input = input("Would you like to search for More movies: (y)es or (n)o? ")



        
            
   

        
