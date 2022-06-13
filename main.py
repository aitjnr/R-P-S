import random

print("Winning Rules of the Rock-Paper-Scissors Game: \n"
+"Rock vs Paper = Paper Wins \n"
+"Rock vs Scissors = Rock Wins \n"
+"Paper vs Scissors = Scissors Wins \n\n")

print("Game Keywords: \n"
+"R = Rock \n"
+"P = Paper \n"
+"S = Scissors \n")

R = "Rock" 
P = "Paper"
S = "Scissors"   

user_action = input("Enter a choice (R, P, S): ")
possible_actions = ["R", "P", "S"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, CPU chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "R":
    if computer_action == "S":
        print("Rock beats scissors! You win!")
    else:
        print("Paper beats rock! You lose.")
elif user_action == "P":
    if computer_action == "R":
        print("Paper beats rock! You win!")
    else:
        print("Scissors beats paper! You lose.")
elif user_action == "S":
    if computer_action == "P":
        print("Scissors beats paper! You win!")
    else:
        print("Rock beats scissors! You lose.")
else: 
    print("Invalid command, not amongst our options. Please, type the correct input.")        
