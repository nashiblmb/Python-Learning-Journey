##Rock Paper Scissors game - Project 4

#import random for computer choice 
import random

#art for rock paper and scissors
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
#add choices into list and input player choice/randomise computer choice
choice_list = (rock, paper, scissors)
player_choice = int(input("Welcome to Rock Paper and Scissors game!\nChoose 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer_choice = random.randint(0,2)

#printing choices for player and computer
print(f"You chose: {choice_list[player_choice]}")
print(f"Computer chose:{choice_list[computer_choice]}")

#logic for playing the game
if computer_choice == player_choice:
    print("It's a draw!")
elif (player_choice == 0 and computer_choice == 2) or \
     (player_choice == 1 and computer_choice == 0) or \
     (player_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose")
