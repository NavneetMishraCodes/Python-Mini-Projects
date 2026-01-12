# this python file has all the functions required for the main game file
# importing required files or modules
import time
import numpy.random as npr

# function to exit in a stylish way on getting an invalid input in format selection
def invalid_input():
    print("Something bad happened !!")
    time.sleep(1)
    print("Select valid choices !!")
    time.sleep(1)
    print("Exiting...")
    print("3")
    time.sleep(1)
    print("2") 
    time.sleep(1)
    print("1")
    time.sleep(1)
    exit()

# function for a round in the game (main function)
def play_game():
    print("You have three choices Snake(S), Water(W) and Gun(G)...")
    user_opt = input("Select anyone of the above by writing its respective symbol(S/W/G): ")
    computer_opt = npr.choice(["S", "W", "G"])
    print(f"Computer Chose: {computer_opt}")
    result = None

    if user_opt == "S":
        if computer_opt == "S":
            print("It's a draw !!")
            result = "D"
        elif computer_opt == "W":
            print("User Wins !!")
            result = "U"
        else:
            print("Computer Wins !!")
            result = "C"

    elif user_opt == "W":
        if computer_opt == "W":
            print("It's a draw !!")
            result = "D"
        elif computer_opt == "G":
            print("User Wins !!")
            result = "U"
        else:
            print("Computer Wins !!")
            result = "C"

    elif user_opt == "G":
        if computer_opt == "G":
            print("It's a draw !!")
            result = "D"
        elif computer_opt == "S":
            print("User Wins !!")
            result = "U"
        else:
            print("Computer Wins !!")
            result = "C"

    else:
        invalid_input()

    return result

