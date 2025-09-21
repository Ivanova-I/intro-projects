import random
computer_secret_number = random.randint(1, 100)
while True:
    player_guess = int(input("Guess a number between 1 and 100: "))
    if player_guess < computer_secret_number:
        print("Your guess is too low.")
    elif player_guess > computer_secret_number:
        print("Your guess is too high.")
    elif player_guess == computer_secret_number:
        print("Congratulations! You guessed my number!")
        break