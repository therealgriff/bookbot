# Function that counts the number of words in the book
def count_words(book_as_string):
    words = book_as_string.split()
    #print(words[:10])  # Print the first 10 words for debugging
    return len(words)


# Function that counts each unique character in the book and return a dictionary with the counts
def count_characters(book_as_string):
    char_count = {}
    for char in book_as_string.lower():
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count


#Function that counts characters in the book and returns a sorted list from most to least common alphabetic characters
def sorted_characters(book_as_string):
    char_count = count_characters(book_as_string)
    # Sort the characters by frequency in descending order
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    # Filter out non-alphanumeric characters
    sorted_chars = [(char, count) for char, count in sorted_chars if char.isalpha()]
    return sorted_chars
# Return a list of tuples (character, count) sorted by count from most to least common
