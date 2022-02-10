# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals

if computer_choice == user_choice : 
     print("Try Again!")

if computer_choice == 'r ' and user_choice == ' s ' :
    print("You lost")
if computer_choice == 's ' and user_choice == ' r ' :
    print("You win")
if computer_choice == 'p ' and user_choice == ' s ' :
    print("You win")