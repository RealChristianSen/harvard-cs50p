
# only using if statements
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

# using elif statements
a = int(input("What's a? "))
b = int(input("What's b? "))

if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
    
# using else statements
c = int(input("What's c? "))
d = int(input("What's d? "))

if c < d:
    print("c is less than d")
elif c > d:
    print("c is greater than d")
else:
    print("c is equal to d")

# using or statement
e = int(input("What's e? "))
f = int(input("What's f? "))

# can also use != or == in this scenario instead of an or statement
if e < f or e > f:
    print("e is not equal to f")
else:
    print("e is equal to f")