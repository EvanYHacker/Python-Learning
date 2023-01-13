import random

computer_score=0
player_score=0
choices = ["rock","paper","scissors"]

print("Game time! Let's play 'Rock, Paper, Scissors'\n")
while player_score <3 and computer_score < 3:
    computer_choice = random.choice(choices)
    player_choice = input("What do you choose: rock, paper or scissors?\n").lower()

    if computer_choice == player_choice:
        print("It's a tie! You both chose "+computer_choice+".")
    elif (computer_choice == "rock" and player_choice=="scissors") or (computer_choice == "paper" and player_choice=="rock") or (computer_choice == "scissors" and player_choice=="paper") :
        computer_score+=1
        print(f"Oh no! The computer beat you! Their {computer_choice} beat your {player_choice}\n You:{player_score} Computer: {computer_score}\n")  
    elif (player_choice == "rock" and computer_choice=="scissors") or (player_choice == "paper" and computer_choice=="rock") or (player_choice == "scissors" and computer_choice=="paper") :
        player_score+=1
        print(f"Congratulations, you won! Your {player_choice} beat their {computer_choice}\n You:{player_score} Computer:{computer_score}\n")       
    else:
        print(f"Sorry, {player_choice} is not a valid choice, please try again\n")  
if computer_score > player_score:
    print(f"The computer won the RPS competition {computer_score} to {player_score}! Better luck next time")
else:
    print(f"You won the RPS competition {player_score} to {computer_score}. You rock!")
