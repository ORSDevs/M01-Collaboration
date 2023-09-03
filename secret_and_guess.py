import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Please guess a number between 1 and 10: "))

    if guess < secret:
        print("too low!")
    elif guess > secret:
        print("too high!")
    else:
        print("Just right!")
        break
