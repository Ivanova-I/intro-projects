import random

name = input("What is your name? ")
print(f'Hello {name}. I wish you good luck!')

words = ['rainbow', 'book', 'read', 'strawberry', 'list', 'luck', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks', 'apology', 'charter', 'drink', 'excavation', 'satisfaction', 'unfair']
word = random.choice(words)
print(f"Guess the word by choosing different letters")

guesses = ''
turns = 10

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    print()

    if failed == 0:
        print("You guessed right!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print(f"You have {turns} more guesses")

        if turns == 0:
            print("You Lose, better luck next time.")
            print(f"The word was: {word}")