"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    print('--------------------------------')
    print('Welcome to number guessing game!')
    print('--------------------------------')

    while True:
        random_number = random.randint(1, 10)
        tries = 0
        high_score = 0

        while True:
            num = input('Pick a number between 1 to 10:  ')

            try:
                num = int(num)
            except ValueError:
                print("Error: Please enter a valid value!\n")
                continue

            if num not in range(1, 11):
                print("The number is outside the range")

            elif num == random_number:
                print(f'\nYou got it! It took you {tries+1} tries')
                break

            elif num > random_number:
                print('It is lower!')
                tries += 1

            elif num < random_number:
                print('It is higher!')
                tries += 1

        if high_score == 0:
            high_score = tries
        elif high_score > tries:
            high_score = tries

        print('\n-x-x-x-x-x-x-x-x-x-x-x-x\n')
        print(f'Your current HIGH SCORE is {high_score+1}')
        print('\nexiting...')
        another_game = input('Would you like to go again [y/n]:  ').lower()
        print()

        if another_game == 'y':
            continue
        break
    print("-----Thank You for playing this game! Hope you enjoyed-----")


# Kick off the program by calling the start_game function.
start_game()
