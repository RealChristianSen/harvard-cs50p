import sys

try:

    if sys.argv[1].endswith(".py") == False:
        sys.exit(1)
        
    if len(sys.argv) > 2:
        sys.exit(1)

    with open(sys.argv[1]) as file:
        lines = file.readlines()

except FileNotFoundError:
    sys.exit(1)

except IndexError:
    sys.exit(1)

count = 0

for line in lines:

    line = line.lstrip()

    if line.startswith("#"):
        continue
    elif line.strip() == "":
        continue
    else:
        count += 1

print(count)
