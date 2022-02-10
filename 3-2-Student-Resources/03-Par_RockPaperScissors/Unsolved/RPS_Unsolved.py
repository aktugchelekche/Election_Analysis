# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["Rock", "Paper", "Scissors"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: Rock, Paper, Scissors? ")

# Run Conditionals
if computer_choice == user_choice : 
     print("Game Tie")


elif user_choice == "Paper" :
    if computer_choice == "Scissors" :
        print(f"You lose , {computer_choice} cut {user_choice} ")
    else : 
         print(f"You win, {user_choice} covers {computer_choice}")
elif user_choice == "Scissors" :
    if computer_choice == "Rock" :
        print(f"You lose , {computer_choice} smashes {user_choice} ")
    else :
        print(f"You win, {user_choice} cuts {computer_choice}")
elif user_choice == "Rock":  
    if computer_choice == "Paper":
        print(f"You lose , {computer_choice} covers {user_choice} ")
    else :
        print(f"You win, {user_choice} smashes {computer_choice} ")





     

