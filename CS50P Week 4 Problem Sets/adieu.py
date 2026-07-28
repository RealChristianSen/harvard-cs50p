import sys
import inflect


def main():

    # creates an instance of the inflect engine class
    p = inflect.engine()
    
    # names list to append the user inputted names to
    names = []

    # while loop to keep prompting until EOFErroe
    while True:
        
        # try except block to catch EOFError
        try:
            user_input = input("Name: ")

            # appends each name into names list
            names.append(user_input)

        # breaks from while loop when EOFError is caught
        except EOFError:
            break
    
    # calls join method on names
    adieu = p.join(names)
    
    # prints concatenated adieu in correct format
    print(f"\nAdieu, adieu, to {adieu}")


main()
