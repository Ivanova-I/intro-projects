import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

# get raw input as a string
player_input = input("Enter your choice: [p]aper, [r]ock or [s]cissors: ")

# map input to the full name
if player_input == "p":
    player_choice = paper
elif player_input == "r":
    player_choice = rock
elif player_input == "s":
    player_choice = scissors
else:
    raise SystemExit("Invalid input! Try again.")

computer_choice = random.choice([rock, paper, scissors])

print(f"You chose: {player_choice}")
print(f"Computer chose: {computer_choice}")


if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == rock:
    if computer_choice == scissors:
        print("You win!")
    else:
        print("You lose!")
elif player_choice == paper:
    if computer_choice == rock:
        print("You win!")
    else:
        print("You lose!")
elif player_choice == scissors:
    if computer_choice == paper:
        print("You win!")
    else:
        print("You lose!")

