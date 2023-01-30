
import random

lower = 1
upper = 100

secret_number = random.randint(lower, upper)

print(f'Guess a number between {lower} and {upper}')

number_of_guesses = 0
while True:

    guess = int(input('What is your next guess? '))
    number_of_guesses += 1

    if guess > secret_number:
        print('lower ...')

    elif guess < secret_number:
        print('higher ...')

    elif guess == secret_number:
        print(f'YEAAAH!!!! The number was {secret_number}. You guessed it in {number_of_guesses} guesses.')
        break
