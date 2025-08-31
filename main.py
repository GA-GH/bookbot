import sys
from stats import number_of_words, sort_char_dict,create_dict


def get_book_text(path_to_file):
    """
    Reads the contents of a file and returns it as a string.

    Args:
        filepath (str): Path to the file.

    Returns:
        str: The entire contents of the file as a string.
    """
    with open(path_to_file, "r", encoding="utf-8") as file:
        return file.read()
    
def main():
    # check command line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    print("============ BOOKBOT ============")
    content = get_book_text(path_to_book)
    print(f"Analyzing book found at books/frankenstein.txt...")
    
    print("----------- Word Count ----------")
    num_words = number_of_words(content)
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    #d = count_of_chars(content)
    #print(d)
    #sort_char_dict(content)
    create_dict()
    sort_char_dict(content)

main()
    