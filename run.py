import random

def get_user_name():

    while True:
        print('Welcome to guess number game')
        print('You can only guess numbers, best of luck!\n')
        print("Enter your name:")
        name = input()
        print(f"Hi {name}! Let's play the game!\n")
        break

        def user_guess(x):
    """
    Function that generates a random number between 1 and 20
    """
    while True:
        try:
            number = random.randint(1, x)
            user_guess = 0
            while user_guess != number:
                user_guess = int(input(f'Make a guess between 1 and {x}:\n'))

                if (user_guess < number):
                    print('Sorry you guessed too low, try again!\n')
                elif (user_guess > number):
                    print('Sorry you guessed too high, try again!\n')
                else:
                    print(f'You guessed correct, it was {number}!\n')
            break
        except ValueError:
            print('Only enter numbers please, try again:')
