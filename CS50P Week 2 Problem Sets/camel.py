# main method to prompt for camelCase str, call convert method on input, and output snake_case str
def main():
    camelCase = input("camelCase: ")
    snake_case = convert(camelCase)
    print(snake_case)

# method to convert camelCase to snake_case
def convert(camelCase):
    
    # converts camelCase to list of char's
    str_list = list(camelCase)
    # list for appended characters for snake_case
    result = []
    
    # iterates through camelCase list
    for char in str_list:
        
        # if the char being iterated is upper case, appends a "_" before the upper case letter
        if char.isupper():
            result.append("_")
        
        # appends the char's in lower case to the result list    
        result.append(char.lower())
    
    # returns the list as a combined string
    return "".join(result)

main()