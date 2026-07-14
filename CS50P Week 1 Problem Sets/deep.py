answer = str(input("What is the Answer to the Great Question of LIge, the Universe, and Everything? "))

answer = answer.lower().strip()

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")