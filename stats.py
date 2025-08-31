import string

list_of_chars=["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", \
    "?", "@", "[", "\\", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",\
        "z", "{", "|", "}", "~", ]

char_dict ={} # Dict to store the frequency of each char

def number_of_words(input_string) -> int:
    """
    Counts the number of words in the given text.
    """
    word_list = input_string.split()
    word_count = 0
    for word in word_list:
        word_count += 1
    return word_count

def sort_char_dict(book_content):
    """ 
    Updates the frequency of each character in the book content and prints out the sorted list in descending order
    """
    list_of_chars = list(book_content)
    
    # update the frequency by 1 if the char is found
    for char in list_of_chars:
        char = char.lower()
        if char in char_dict:
            char_dict[char]["num"] += 1
    
    #TODO understand the code
    # sort the dict
    sorted_dict = {
        entry["char"]: entry
        for entry in sorted(
            #(v for k, v in char_dict.items() if k in string.ascii_lowercase),
            (v for k, v in char_dict.items() if k.isalpha()),
            key=lambda x: x["num"],
            reverse=True   # highest first
        )
    }
    
    # print the report
    for key, value in sorted_dict.items():
        print(f"{key}: {value["num"]}")
    
def create_dict():
    """
    create the dict to be used to print the result from the list of chars
    """
    for ch in list_of_chars:
        char_dict[ch] = {"char" : ch, "num" : 0}   
