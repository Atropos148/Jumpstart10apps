import random

print('--------------------------------')
print('    GUESS THAT NUMBER GAME')
print('--------------------------------')
print()

chosen_number = random.randint(0, 100)
guess_int = -1

while guess_int != chosen_number:
    guess_text = input('Guess the number between 0 and 100: ')
    try:
        guess_int = int(guess_text)
    except ValueError:
        print("That is not a number")

    if guess_int < chosen_number:
        print('Your guess of {} is too LOW'.format(guess_int))
    elif guess_int > chosen_number:
        print('Your guess of {} is too HIGH'.format(guess_int))
    elif guess_int == chosen_number:
        print('Correct! You win! The number was {}!'.format(chosen_number))
