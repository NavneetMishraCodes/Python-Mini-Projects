# importing the required libraries
import random
import time

# introducing
print("Welcome To Random Number Guess Game...")
print()

# generating the random number
rand_num = random.randint(1, 100)

# now allowing user to play
attempts = 1

# game loop
while True:
    user_num = int(input(f"Guess Number (Attempt - {attempts}): "))

    if user_num < rand_num:
        print("Too Low !")
    elif user_num > rand_num:
        print("Too High !")
    else:
        print("You Got It !")
        break

    attempts += 1

print()
print(f"You guessed the correct number in {attempts} attempts.")
print("!! :) Congratulations & Thankyou (: !!")
print()

# taking user's name
user_name = input("Your Name: ")

# saving the history
with open("D:\\Python_Programming\\Mini_Projects\\Random_Number_Guess_Game\\history.txt", "a") as f:
    f.write(f"Username : {user_name}\n")
    f.write(f"Attempts Took To Guess Right : {attempts}\n")
    f.write("\n")

print("History Saved...")
time.sleep(3)
