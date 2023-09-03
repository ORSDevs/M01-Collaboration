guess_me = 5

while True:
    user_guess = int(input("Please guess the number: "))

    if user_guess < guess_me:
        print('Too low.')
    elif user_guess == guess_me:
        print('Found it!')
        break
    else:
        print('Oops!')