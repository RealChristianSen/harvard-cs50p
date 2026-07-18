def main():
    print_square(3)
    
def print_square(size):
    
    # creates rows
    for i in range(size):
        
        # creates squares in row
        for j in range(size):
            print("#", end="")
        # creates new line
        print("")
    
main()