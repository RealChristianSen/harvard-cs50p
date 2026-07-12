y = input("What's y? ")
x = input("What's x? ")

# will return x and y concatenated as strings instead of actually adding
z = x + y
print(z)

# will return x and y added as integers instead of concatenated as strings
r = int(x) + int(y)
print(r)

# can instead put the int() function around the input() function 
# to convert the input to an integer immediately instead of converting it later
p = int(input("What's p? "))
o = int(input("What's o? "))
print(p + o)


# can also use float() to convert the input to a decimal number/floating point value
# instead of an integer
a = float(input("What's a? "))
b = float(input("What's b? "))

# can use the round() function to round a number to a certain number of decimal places, by default
# it rounds to the nearest whole number
u = round(a + b)
# can also specify the number of decimal places to round to by passing a
# second argument to the round() function
u1 = round(a + b, 2)

print(u)
print(u1)

y = 1000000
# can use the comma as a thousands separator in a number by using the :, format specifier
print(f"{y:,}")


q = 2
e = 3
# simple division
z = q / e

# can use the :.2f format specifier to round a number to 2 decimal places
# can be used to avoid infinite decimal places when dividing numbers that don't divide evenly
print(f"{z:.2f}")