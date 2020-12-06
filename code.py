#Rock Paper Scissors V2.0
#Player VS Computer

#Allowing the use of random selection
import random

gameOptions = ["rock", "paper", "scissors"]

player1Choice = input("To play choose \"Rock\", \"Paper\" or \"Scissors\" ->").lower()

#Checking Player 1 choice
while (player1Choice != "rock" and player1Choice != "paper" and player1Choice != "scissors") :
    print("That\'s not a correct choice, try again please.")
    player1Choice = input("To play choose \"Rock\", \"Paper\" or \"Scissors\" ->").lower()

computerChoice = random.choice(gameOptions)

print("Player:", player1Choice, "VS","Computer:", computerChoice)

#Checking for a winner
if player1Choice == "rock" and computerChoice == "paper" :
    print("Paper covers rock, Computer wins!")

elif player1Choice == "rock" and computerChoice == "scissors" :
    print("Rock crushes scissors, Player wins!")

elif player1Choice == "paper" and computerChoice == "scissors" :
    print("Scissors cut paper, Computer wins!")

elif player1Choice == "paper" and computerChoice == "rock" :
    print("Paper covers rock, Player wins!")

elif player1Choice == "scissors" and computerChoice == "rock" :
    print("Rock crushes scissors, Computer wins!")

elif player1Choice == "scissors" and computerChoice == "paper" :
    print("Scissors cut paper, Player wins!")

else :
    print("Draw!")