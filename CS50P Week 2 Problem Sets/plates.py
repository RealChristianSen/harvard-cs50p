# main function to prompt user for plate and output whether it's valid or invalid
def main():
    
    plate = input("Plate: ")
    
    if is_valid(plate):
        print("Valid")
        
    else:
        print("Invalid")


# function to return if the plate is valid or not
def is_valid(s):
    
    # boolean expression returning True or False based on the outcome of the check functions
    if length(s) == True and starting(s) == True and order(s) == True and punctuation(s) == True:
        return True
    else:
        return False
        
# function that returns True if the plate meets the length requirements, false if not
def length(s):
    
    # boolean expression checking the length of the plate
    if len(s) > 2 and len(s) < 7:
        return True
    else:
        return False

# function that returns True if the first two char's are non digits, if not False
def starting(s):
    
    # boolean expression checking the char type at indices 0 and 1
    if s[0].isdigit() or s[1].isdigit():
        return False
    else:
        return True

# function that returns True if there are no numbers in the middle of the plate, False if not
def order(s):
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
    
    return True


# function that returns True if there is no punctuation used, False if not
def punctuation(s):
    # list of common punctuationsCS05
    list = [".", " ", "!", "?", ",", "_", "$"]
    
    # loop that indices through s
    for i in s:
        
        # boolean expressions to return False if there is a punctuation in the plate
        if i not in list:
            ...
        else:
            return False
    
    return True

main()