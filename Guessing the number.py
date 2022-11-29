import random

def guess(x):
    random_number = random.randint(1,x)
    #random.randint returns a random no. for us to guess
    guess = 0
    #because we don't want our guess to be accidentally equal to the number
    while guess != random_number:
        guess = input(f'Guess a number between 1 and {x}: ')
        if guess < random_number:
            print("Sorry, guess again. Too Low")
        elif guess > random_number:
            print("Sorry, guess again. Too High")

    print("Congrats! you have guessed the number correctly: ")

guess(10)