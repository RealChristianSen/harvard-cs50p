# define list of vowels
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# main method to prompt user input and call on omit_vowel method and then print the result
def main():
    user_input = input("Input: ")
    print(f"Output: {omit_vowel(user_input)}", end ="")

# omit_vowel method that converts user input to a list, iterates through the list 
# omitting every vowel and return the list as a combined string
def omit_vowel(word):
    
    # converts string to list
    word = list(word)
    
    # new list for appended char's
    without_vowels = []
    
    # iterates through every single char in word list
    for char in word:
        
        # boolean expression to check if each char is a vowel or not, if not then append to new list
        if char not in vowels :
                without_vowels.append(char)
    
    # returns the list as a joined string
    return"".join(without_vowels)
    
main()