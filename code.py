#Rock Paper Scissors V3.0
#Player VS Computer
#Now with rounds

#Allowing the use of random selection
import random

gameOptions = ["rock", "paper", "scissors"]

playerScore = 0
computerScore = 0

roundsChoice = -1

while (roundsChoice < 0) : 
    try:
        roundsChoice = int(input("Please choose how many rounds you want to play \n(1, 2 or more) or '0' to exit-> "))
        print("")
        if roundsChoice == 0 :
            exit()
    except ValueError:
        print("")
        print("That's not a number, choose a number or '0' to exit->")
        print("")

playerChoice = input("Choose 'Rock', 'Paper' or 'Scissors' -> ").lower()
print("")

#Checking Player 1 choice
while (playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors") :
    print("That\'s not a correct choice, try again please.")
    playerChoice = input("To play choose 'Rock', 'Paper' or 'Scissors' ->").lower()
    print("")

computerChoice = random.choice(gameOptions)

print("Player:", playerChoice, "VS","Computer:", computerChoice)
print("")

#Checking for a winner
if playerChoice == "rock" and computerChoice == "paper" :
    print("Paper covers rock, Computer wins!")

elif playerChoice == "rock" and computerChoice == "scissors" :
    print("Rock crushes scissors, Player wins!")

elif playerChoice == "paper" and computerChoice == "scissors" :
    print("Scissors cut paper, Computer wins!")

elif playerChoice == "paper" and computerChoice == "rock" :
    print("Paper covers rock, Player wins!")

elif playerChoice == "scissors" and computerChoice == "rock" :
    print("Rock crushes scissors, Computer wins!")

elif playerChoice == "scissors" and computerChoice == "paper" :
    print("Scissors cut paper, Player wins!")

else :
    print("Draw!")