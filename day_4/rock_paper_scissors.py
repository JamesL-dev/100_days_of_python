################################# 
# Rock Paper Scissors program
#
################################# 
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
player_choice_as_int = int(player_choice)

if player_choice_as_int >= 3 or player_choice_as_int < 0:
    print("You typed an invalid number, you lose!")
else:
    print(f"You chose: {choices[player_choice_as_int]}")
    computer_choice = random.randint(0,2)
    print(f"Computer Chose: {choices[computer_choice]}")

    if player_choice_as_int == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and player_choice_as_int == 2:
        print("You lose!")
    elif computer_choice > player_choice_as_int:
        print("You Lose!")
    elif computer_choice == player_choice_as_int:
        print("Draw!")

