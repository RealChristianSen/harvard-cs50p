import random
import sys


def main():

    # while loop to keep looping until user enters positive int input
    while True:

        # try except block to catch if user enters a non int input
        try:
            n = int(input("Level: "))

            # catches if user enters a non positive int input and continues if not
            if n <= 0:
                continue

            # calls guess function if user input is valid
            else:
                guess(n)

        # catches ValueError
        except ValueError:
            continue


# guess function to take user input and match it with a random integer
def guess(n):

    # produces a random integer in 1 and n inclusive
    integer = random.randint(1, n)

    # while loop to keep prompting for guess if not valid, or until correct guess is entered
    while True:

        # try except block to catch ValueErrors
        try:
            guess = int(input("Guess: "))

            # catches if user guess is non-positive
            if guess <= 0:
                continue

            # else outputs if user's guess is incorrect or correct
            else:
                if guess < integer and guess > 0:
                    print("Too small!")
                    continue

                elif guess > integer:
                    print("Too large!")
                    continue

                else:
                    print("Just Right!")
                    sys.exit()

        # catches ValueError
        except ValueError:
            continue


main()
