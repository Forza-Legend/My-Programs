from random import randint
from typing import Counter
import os

print("Hi")
os.system('CLS')

def skip(any):
    skip
no = False
yes = True
difference = 0
options = ["Rock","Paper","Scissors"]
counter = 10
player_score = 0
computer_score = 0
computer_input = " "
user_input = " "
loop = ["f","f","f","f","f","f","f","f","f","f"]

while counter == 10:

    for f in loop:

        print(f"Option = {options}")
        user_input = input("Type your option: ")

        value = randint(1,3)

        if value == 1:
            computer_input = "Rock"

        elif value == 2:
            computer_input = "Paper"

        else:
            computer_input = "Scissors"

        print(computer_input)

        if computer_input == user_input:
            print("Draw")

        elif computer_input == "Rock":
            if user_input == "Paper":
                print("You win")
                player_score += 1
                print(f"Your score is: {player_score}")
                print(f"My score is: {computer_score}")
            elif user_input == "Scissors":
                print("You lose")
                computer_score += 1
                print(f"Your score is: {player_score}")
                print(f"My score is: {computer_score}")
            else:
                print("Invalid Input")

        elif computer_input == "Paper":
            if user_input == "Scissor":
                print("You win")
                player_score += 1
                print(f"Your score is: {player_score}")
                print(f"My score is: {computer_score}")
            elif user_input == "Rock":
                print("You lose")
                computer_score += 1
                print(f"Your score is: {player_score}")
                print(f"My score is: {computer_score}")
            else:
                print("Invalid Input")

        elif computer_input == "Scissor":
            if user_input == "Paper":
                print("You lose")
                computer_score += 1
                print(f"Your score is: {player_score}")
                print(f"My score is: {computer_score}")
            elif user_input == "Rock":
                print("You win")
                player_score += 1
                print(f"Your score is: {player_score}")
                print(f"My score is: {computer_score}")
            else:
                print("Invalid Input")
        
    play_again = input("Do you want to play again: ")

    if play_again == "no":
        counter += 1
    elif play_again == "yes":
        skip(any)
    else:
        print("Invalid Input")
        

if player_score > computer_score:
    difference = player_score - computer_score
    print("Congrats, You Win")
    print(f"You win by {difference}")

elif computer_score > player_score:
    difference =  computer_score - player_score
    print("Better luck next time")
    print(f"You lost by {difference}")

else:
    print("Draw")
    print(f"Score:{player_score}")