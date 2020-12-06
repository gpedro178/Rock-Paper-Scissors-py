#Rock Paper Scissors V3.0
#Player VS Computer
#Now with rounds!

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

startingRoundNumber = 0

while (startingRoundNumber < roundsChoice) :
    print("ROUND:", startingRoundNumber + 1)

    playerChoice = input("Choose 'Rock', 'Paper' or 'Scissors' -> ").lower()
    print("")

    #Checking Player 1 choice
    while (playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors") :
        print("That's not a correct choice, try again please.")
        playerChoice = input("Choose 'Rock', 'Paper' or 'Scissors' -> ").lower()
        print("")

    computerChoice = random.choice(gameOptions)

    print("Player:", playerChoice, "VS","Computer:", computerChoice)
    print("")

    #Checking for a winner
    if playerChoice == "rock" and computerChoice == "paper" :
        print("Paper covers rock, Computer win this round!")
        computerScore += 1
        print("")

    elif playerChoice == "rock" and computerChoice == "scissors" :
        print("Rock crushes scissors, Player win this round!")
        playerScore += 1

    elif playerChoice == "paper" and computerChoice == "scissors" :
        print("Scissors cut paper, Computer win this round!")
        computerScore += 1

    elif playerChoice == "paper" and computerChoice == "rock" :
        print("Paper covers rock, Player win this round!")
        playerScore += 1

    elif playerChoice == "scissors" and computerChoice == "rock" :
        print("Rock crushes scissors, Computer win this round!")
        computerScore += 1

    elif playerChoice == "scissors" and computerChoice == "paper" :
        print("Scissors cut paper, Player win this round!")
        playerScore += 1

    else :
        print("Draw! No points!")
    
    #Printing Score
    print("Player Score:", playerScore, " ", "Computer Score:", computerScore)
    print("")

    startingRoundNumber += 1

#Setting final score
if (playerScore > computerScore) :
    print("The final score show that you have beaten the computer!")
elif (playerScore < computerScore) :
    print("The final score show that the computer have won this time!")
else :
    print("The final score show that this ended in a draw!")