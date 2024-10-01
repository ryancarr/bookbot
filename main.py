def count_words(text: str) -> int:
    """
    This function receives a block of text and counts the number of words returning an integer.
    
    Args:
        text (str): A block of text that needs the words counted.
        
    Returns:
        int: An integer representing the total number of words found in the input text.
    """
    return len(text.split())

def count_characters(text: str, symbols: bool =True) -> dict[str, int]:
    """
    This function counts the number of individual characters in a block of text. All characters
    are treated as lowercase. Instructions weren't clear how to handle numbers, symbols or
    spaces, so all characters are counted.
    
    Args:
        text (str): The input block of text that you need a character count
        symbols (bool): Optional argument that determine if nonalpha characters are included.
        
    Returns:
        dict (str, int): A dictionary where characters are the keys and values are how 
        many times the letter is seen.
    """
    output = {}
    
    text = text.lower()

    for letter in text:
        # If we are excluding symbols and the current letter is not in the alphabet skip
        # current letter
        if not symbols and not letter.isalpha():
            continue
        
        # Update the value of the character. If a character hasn't been seen yet 
        # default to 0 and add 1
        output[letter] = output.get(letter, 0) + 1
    
    return output

def sort_char_dictionary(character_dict: dict[str, int]) -> dict[str, int]:
    """
    Takes an unsorted dictionary of characters, removing non alphanumeric characters and
    sort based on character frequency.
    
    Args:
        dict (str, int): A dictionary that is unsorted made of string, int pairs.
        
    
    Returns:
        dict (str, int): A sorted dictionary, sorted in reverse value order.
    """
    return dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True))


filename = 'books/frankenstein.txt'

try:
    with open(filename) as fh:
        text = fh.read()

    word_count = count_words(text)
    character_dict = count_characters(text, False)
except FileNotFoundError:
    print(f"Error: The file {filename} was not found.")
    exit()

output = sort_char_dictionary(character_dict)

print(f"--- Begin report of {filename} ---")
print(f"{word_count} words found in the document\n")

for k, v in output.items():
    print(f"The '{k}' character was found {v} times")

print("--- End report ---")