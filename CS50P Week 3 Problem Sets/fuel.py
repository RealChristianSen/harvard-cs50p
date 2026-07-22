# main fnc to prompt user input, hold while loop, catch errors, and call on convert fnc
def main():
    
    # while statement to keep prompting user until input is valid
    while True:
        try:
            gas_fraction = input("Fraction: ")
            
            # converts fraction into seperated x and y
            x, y = gas_fraction.split("/")
            x = int(x)
            y = int(y)
            
            # if y is less than x, x is less than 0, or y is less than 0, continues to re-prompt user
            if y < x or x < 0 or y < 0:
                continue
            # else calls convert function on x and y and prints result
            else:
                print(f"{convert(x, y)}")
                break
        
        # handles ValueError
        except ValueError:
            pass
        
        # handles ZeroDivisionError
        except ZeroDivisionError:
            pass

# convert fnc to return F, E, and a percentage depending on the user input
def convert (x, y):
    
    # converts fraction into percentage
    gas_percent = (x / y) * 100
    
    # returns F if x and y are equal or percentage is greater than or equal to 99
    if x == y or gas_percent >= 99:
        return "F"
    
    # returns E if x is 0 or percentage is less than or equal to 1
    if x == 0 or gas_percent <= 1:
        return "E"

    # returns percentage rounded with percentage sign
    return f"{gas_percent:.0f}%"

main()