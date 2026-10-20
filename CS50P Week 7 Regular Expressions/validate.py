import re

email = input("what's youre email?").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")