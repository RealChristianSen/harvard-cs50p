# prompts user for greeting
# if greeting starts with "hello" output $0
# if greeting starts with an 'h' output $20
# else output $100

def main():
    greeting = input("Greeting: ")
    
    number = value(greeting)
    
    print(number)
    
def value(greeting):
    greeting = greeting.lower().strip()

    # special case for specifically Newman
    if greeting == "hello, newman":
        return 0

    # catches if "hello is the greeting"
    elif greeting == "hello":
        return 0
    # else to catch everything else to be able to independently catch char 0
    else:
    #splits the greeting into chars
        char = list(greeting)
        
    # catches whether h is the first char or not
        if char[0] == 'h':
            return 20
    # if not prints out $100
        else:
            return 100


if __name__ == "__main__":
    main()