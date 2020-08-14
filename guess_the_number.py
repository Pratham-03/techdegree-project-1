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
    high_score = 0

    name = str(input('Please enter to your name to begin:  '))

    print('_______________________________________________________________________________________________________')
    print("""
 _____ _        _  _            _              ___                _            ___                
|_   _| |_  ___| \| |_  _ _ __ | |__  ___ _ _ / __|_  _ ___ _____(_)_ _  __ _ / __|__ _ _ __  ___ 
  | | | ' \/ -_) .` | || | '  \| '_ \/ -_) '_| (_ | || / -_|_-<_-< | ' \/ _` | (_ / _` | '  \/ -_)
  |_| |_||_\___|_|\_|\_,_|_|_|_|_.__/\___|_|  \___|\_,_\___/__/__/_|_||_\__, |\___\__,_|_|_|_\___|•••
                                                                        |___/  
    """)
    print(f'Hi there {name}, welcome to the number guessing game!')
    print('_______________________________________________________________________________________________________\n')

    while True:
        random_number = random.randint(1, 10)
        tries = 0

        while True:
            num = input('Pick a number between 1 to 10:  ')

            try:
                num = int(num)
            except ValueError:
                print("Error: Please enter a valid value!\n")
                continue

            if num not in range(1, 11):
                print("\nThe number is outside the range")

            elif num == random_number:
                print(f'\nCongrats {name} you got it! The number was {num}')
                tries += 1
                break

            elif num > random_number:
                print(f"It's higher! Guess a number lower than {num}\n")
                tries += 1

            elif num < random_number:
                print(f"It's lower! Guess a number higher than {num}\n")
                tries += 1
        
        if tries == 1:
            print(f'Nice Work! It took you {tries} try.')
        else:  
            print(f'Nice Work! It took you {tries} tries.')
        
        if high_score == 0:
            high_score = tries
        elif tries < high_score:
            high_score = tries

        print('\n_______________________________________________________________________________________________________\n')
        print('\nexiting...')
        another_game = input("Would you like to go again? Please enter 'y' to continue or any other key to quit:  ").lower()
        print()

        print(f'\nYour HIGH SCORE is {high_score}!\n')

        if another_game == 'y':
            continue
        break
    print(f"-----Thank You {name} for playing this game! Hope you enjoyed-----")


# Kick off the program by calling the start_game function.
start_game()
