list = {}

def main():
    
    # while loop to keep prompting user until user hits ctrl d
    while True:
        
        # try except block to catch EOFError from ctrl d, else continue running
        try:
            
            # prompts user input and titles it
            item = input("")
            item = item.upper()
            
            # boolean expressions to add item to grocery list, if already exists add 1 to it's count
            if item in list:
                list[item] = list[item] + 1
            
            else:
                list[item] = 1
        
        # catches EOFError
        except EOFError:
            break
    
    # prints the list sorted alphabetically along with the associated count
    for item in sorted(list):
        print(list[item], item)
    
main()