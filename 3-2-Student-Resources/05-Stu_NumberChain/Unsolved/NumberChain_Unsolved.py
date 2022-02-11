# Initial variable to track game play
user_play = "y"
user = 0
# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_input = int(input("How many Numbers to loop through!"))
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for number in range(user,user_input+user+1):
        

        # Print each number in the range
        print(number)
    
   
    # Once complete...
    
    user_play = input("Continue: (y)es or (n)o? ")
    if user_play == "y" :
        user= user_input


    
    
        