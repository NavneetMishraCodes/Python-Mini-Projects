# importing required files or modules
import functions as fn
import time

# introducing the game
print("Welcome to Snake, Water and Gun Game !!")
print()
print("The game has following three formats (select any one by writing its respective char) :- ")
print("a - One Round")
print("b - Three Rounds")
print("c - Five Rounds")
print("")

game_format = input("Enter the format of the game you like to play: ")
print("")

# main game
score_card = {"User" : 0, "Computer" : 0, "Draw" : 0}
if game_format == 'a':
    curr = fn.play_game()
    if curr == "U":
        score_card["User"] += 1
    elif curr == "C":
        score_card["Computer"] += 1
    else:
        score_card["Draw"] += 1
    print("")

elif game_format == 'b':
   curr = None
   for i in range(0, 3):
        curr = fn.play_game()
        if curr == "U":
            score_card["User"] += 1
        elif curr == "C":
            score_card["Computer"] += 1
        else:
            score_card["Draw"] += 1
        print("")
       
elif game_format == 'c':
    curr = None
    for i in range(0, 5):
        curr = fn.play_game()
        if curr == "U":
            score_card["User"] += 1
        elif curr == "C":
            score_card["Computer"] += 1
        else:
            score_card["Draw"] += 1
        print("") 

else:
    fn.invalid_input()

# showing final result
print("Final Score Card :-")
for key, value in score_card.items():
    print(f"\t{key} : {value}")
print("")

user_points = score_card["User"] + (0.5 * score_card["Draw"])
computer_points = score_card["Computer"] + (0.5 * score_card["Draw"])

print(f"User Points: {user_points}")
print(f"Computer Points: {computer_points}")
print("")

if user_points > computer_points:
    print("USER WINS !!")
elif computer_points > user_points:
    print("COMPUTER WINS !!")
else:
    print("ITS A DRAW !!")

print("")
print("Check the result, you have 15s...")
time.sleep(15)
