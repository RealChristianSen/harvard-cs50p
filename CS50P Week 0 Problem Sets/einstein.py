#prompts the user for mass and outputs the equivalent number of joules as an int

def main():
    #take mass input and call on convert to get equivalent number of joules and print it
    mass = int(input("m: "))
    joules = convert(mass)
    
    print("E: ", joules)
    
def convert(m):
    #recieves mass variable and converts it to amount of joules
    c = 300000000 * 300000000
    return m * c

main()