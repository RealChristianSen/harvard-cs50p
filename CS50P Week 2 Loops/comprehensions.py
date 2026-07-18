def main():
    words = get_words("address.txt")
    
    # list comprehension: builds a new list with only words longer than 4 chars, lowercased

    lowercase_words = [word.lower() for word in words if len(word) > 4]
    
    # dict comprehension: builds a dict where each word is a key, mapped to how many times it appears
    counts = {word: words.count(word) for word in words}
    
    save_counts(counts)

def get_words():
    ...

def save_counts(counts):
    ...

main()