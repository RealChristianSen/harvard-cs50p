# main function to prompt user for plate and output whether it's valid or invalid
def main():

    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")

    else:
        print("Invalid")


# function to return if the plate is valid or not
def is_valid(s):
    list = [".", " ", "!", "?", ",", "_", "$", "/"]

    # boolean expression checking the length of the plate
    if len(s) <= 2 or len(s) >= 7:
        return False

    # boolean expression checking the char type at indices 0 and 1
    if s[0].isdigit() or s[1].isdigit():
        return False

    seen_digit = False
    # for loop indicing through s
    for i in s:

        # returns False if the indexed char is 0
        if i == "0" and seen_digit == False:
            return False

        # if a char is a digit sets seen_digit to True
        if i.isdigit():
            seen_digit = True

        # if seen_digit is true and the char at the index is a non digit, return False
        if seen_digit == True and i.isalpha():
            return False

    # loop that indices through s
    for i in s:

        # boolean expressions to return False if there is a punctuation in the plate
        if i in list:
            return False

    return True


if __name__ == "__main__":
    main()