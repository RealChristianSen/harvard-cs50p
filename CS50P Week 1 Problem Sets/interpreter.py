# prompts user for expression
expression = input("Expression: ")

# fixes user error in input
expression = expression.strip()

# splits expression to seperate variables and type of expression
x, y, z = expression.split()

# converts variables into floats
x = float(x)
z = float(z)

# booleans to calculate based on expression type
if y == "+":
    print(f"{x + z:.1f}")

elif y == "-":
    print(f"{x - z:.1f}")

elif y == "*":
    print(f"{x * z:.1f}")

elif y == "/":
    print(f"{x / z:.1f}")