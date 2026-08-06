import random

rock = 1
scissors = 2
paper = 3

while True:
    ai = random.randint(1, 3)
    player = int(input("0.exit 1.rock 2.scissors 3.paper: "))

    if player == 0:
        print("Game Over")
        break
    elif player not in [1, 2, 3]:
        print("Please choose a valid number")
        continue

    # AI chooses Rock (1)
    if ai == 1 and player == 1:
        print("AI: Rock | You: Rock -> Draw")
    elif ai == 1 and player == 2:
        print("AI: Rock | You: Scissors -> AI Wins!")
    elif ai == 1 and player == 3:
        print("AI: Rock | You: Paper -> You Win!")

    # AI chooses Scissors (2)
    elif ai == 2 and player == 1:
        print("AI: Scissors | You: Rock -> You Win!")
    elif ai == 2 and player == 2:
        print("AI: Scissors | You: Scissors -> Draw")
    elif ai == 2 and player == 3:
        print("AI: Scissors | You: Paper -> AI Wins!")

    # AI chooses Paper (3)
    elif ai == 3 and player == 1:
        print("AI: Paper | You: Rock -> AI Wins!")
    elif ai == 3 and player == 2:
        print("AI: Paper | You: Scissors -> You Win!")
    elif ai == 3 and player == 3:
        print("AI: Paper | You: Paper -> Draw")
      
