def main():
    
# prompts user for time
    time = input("What time is it? ")
    
# passes time to convert function
    totalTime = convert(time)

# boolean expressions to determine if it is breakfast time, lunch time, dinner time, or none
    if totalTime <= 19 and totalTime >= 18:
        print("dinner time")

    elif totalTime <= 13 and totalTime >= 12:
        print("lunch time")

    elif totalTime <= 8 and totalTime >= 7:
        print("breakfast time")

    else:
        print("")

def convert(time):
    
# splits the time string to hours and minutes to be able to convert to a number to be computed
    hours, minutes = time.split(":")

# converts hours and minutes to floats
    hours = float(hours)
    minutes = float(minutes)

# returns the time after being calculated
    return ((hours * 60) + minutes) / 60

if __name__ == "__main__":
    main()
