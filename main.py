# BookBot: A simple program to analyze a book's text
# Usage: python main.py <path_to_book>

#import sys module for sys.argv
import sys

# Import count_words and sorted_characters from stats.py
from stats import count_words
from stats import sorted_characters

def main():
    # Check if the user provided a book path
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the book path as CL arguments
    book_path = sys.argv[1]

    # Import the book as a string
    book_as_string = import_book(book_path)
    
    # Start formating the output
    print("============ BOOKBOT ============")

    # Print the path to the book
    print(f"Analyzing book found at {book_path}...")

    # Count the words in the book
    word_count = count_words(book_as_string)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    # Count the characters in the book
    print("--------- Character Count -------")
    for char, count in sorted_characters(book_as_string):
        print(f"{char.lower()}: {count}")
    
    # End of the analysis
    print("============= END ===============")

# Function to import the book from a given path
def import_book(path):
    with open(path, 'r') as file:
        book_as_string = file.read()
    return book_as_string



main()

