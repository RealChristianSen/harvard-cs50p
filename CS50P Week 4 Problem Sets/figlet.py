import pyfiglet
from pyfiglet import Figlet
import sys
import random


def main():

    # creates object of Figlet class from the pyfiglet package
    figlet = Figlet()
    
    # assigns fonts variable with all fonts
    fonts = figlet.getFonts()
    
    # assigns font with a randomly chosen font from fonts
    font = random.choice(fonts)

    # if user enters 0 arguments
    if len(sys.argv) == 1:
        user_input = input("Input: ")
        # formats user input with a randomly chosen font in figlet format and prints it
        f = pyfiglet.figlet_format(user_input, font)
        print(f)

    # catches if user does not enter 2 arguments, if the 1st argument is not -f or --font, and if the 2nd argument is not in fonts
    elif (
        len(sys.argv) != 3
        or sys.argv[1] not in ("-f", "--font")
        or sys.argv[2] not in fonts
    ):
        # exits code
        sys.exit(1)

    # if user enters 2 arguments
    else:
        user_input = input("Input: ")
        # formats uer input with chosen font in figlet format and prints it
        f = pyfiglet.figlet_format(user_input, font=sys.argv[2])
        print(f)


main()
