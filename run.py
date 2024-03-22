import random

def get_user_name():

    while True:
        print('Welcome to guess number game')
        print('You can only guess numbers, best of luck!\n')
        print("Enter your name:")
        name = input()
        print(f"Hi {name}! Let's play the game!\n")
        break