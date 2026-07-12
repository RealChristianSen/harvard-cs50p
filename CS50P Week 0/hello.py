print("Hello, World!")

# ask user for their name
name = input("What is your name? ")

#  whitespace from string
name = name.strip()

# capitalize user's name
name = name.capitalize() 

# capitalize first letter of each word in user's name
name = name.title()

# can chain methods together
name = name.strip().title()

# split user's name into first and last name
first, last = name.split(" ")

name = input("What's your name? ").strip().title()

# print their name 
print("Hello, " + name)
print("Hello,", name)
print(f"Hello, {name}")
print("Hello,", name, sep = "_", end = "!\n" )
print(f"Hello, {first}")