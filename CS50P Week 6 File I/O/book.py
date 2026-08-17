def main():
    with open("alice.txt") as f:
        contents = f.readlines()
        
    chapter1 = contents[52:272]
    with open("chapter1.txt", "w") as f:
        f.write(chapter1)


main()