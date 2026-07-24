import requests
import emoji


def main():
    name = input("Input: ")

    # calls on emoji module to use emojize function to convert string to emoji as well as aliases
    user_emoji = emoji.emojize(name, language="alias")

    # prints out converted emoji
    print(f"{user_emoji}")


main()
