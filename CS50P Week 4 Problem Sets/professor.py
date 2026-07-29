import random


def main():

    # list for dictionaries of x y and z numbers
    problems = []

    # calls get_level function and assigns returned var to level
    level = get_level()

    # defines correct var for correct user answers
    correct = 0

    # for loop that loops 10 times for each randomly generated problem
    for i in range(10):
        
        # calls on generate_integer function to assign x a random int
        x = generate_integer(level)
        
        # calls on generate_integer function to assign y a random int
        y = generate_integer(level)
        
        # assigns z the sum of x and y
        z = x + y
        
        # assigns the problem dict's keys with it's associated values
        problem = {'x': x, 'y': y, 'z': z}
        
        # appends the problem dict to the problems list
        problems.append(problem)

    # for loop to iterate through the 10 problems in the problems list
    for problem in problems:
        
        # sets incorrect var to 0 each correct user answer
        incorrect = 0

        # while the user has entered less than 3 wrong answers keep looping
        while incorrect < 3:

            # try except block to catch ValueError
            try:
                user_answer = int(input(f"{problem['x']} + {problem['y']} = "))

            # catches ValueError and continues to reprompt and prints EEE
            except ValueError:
                print("EEE")
                incorrect += 1
                continue
            
            # if user answers correctly increments correct var
            if user_answer == problem["z"]:
                correct += 1
                break
            
            # if user answers incorrectly increments inocorrect var and prints EEE
            else:
                print("EEE")
                incorrect += 1
                
        # if user answers incorrectly 3 times displays the correct answer
        else:
            print(f"{problem['x']} + {problem['y']} = {problem['z']}")

    # after 10 problems have been solved incorrectly or correctly prints out the user score out of 10
    print(f"Score: {correct}")

# function to prompt user for level, reprompt if necessary, and returns the level
def get_level():

    # while loop to keep reprompting user until valid level is entered
    while True:

        try:
            level = int(input("Level: "))

            # if level is not 1, 2, or 3 continues to reprompt
            if level not in [1, 2, 3]:
                continue
            
            # returns level if valid
            else:
                return level

        # catches ValueError and continues while loop
        except ValueError:
            continue

# function to return randomly generated integer
def generate_integer(level):

    # returns randomly generated integer based on the level
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    
    # if level is not valid raises ValueError
    else:
        raise ValueError


main()
