def main():
    #prompts user for input, calls convert on input, and prints the result
    phrase = input("Please enter the phrase: ")
    print(convert(phrase))

def convert(phrase):
    #accepts a str and returns any input with :) or :( into their respective emoticons
    return phrase.replace(":)", "🙂").replace(":(", "🙁")

main()