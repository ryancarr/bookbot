def count_words(text: str) -> int:
    """
    This function receives a block of text and counts the number of words returning an integer.
    
    Args:
        text (str): A block of text that needs the words counted.
        
    Returns:
        int: An integer representing the total number of words found in the input text.
    """
    return len(text.split())

def count_characters(text: str) -> dict[str, int]:
    """
    This function counts the number of individual characters in a block of text. All characters
    are treated as lowercase. Instructions weren't clear how to handle numbers, symbols or
    spaces, so all characters are counted.
    
    Args:
        text (str): The input block of text that you need a character count
        
    Returns:
        dict (str:int): A dictionary where characters are the keys and values are how many times the
        letter is seen.
    """
    output = {}
    
    for letter in text.lower():
        # Update the value of the letter. If a letter hasn't been seen yet default to 0 and add 1
        output[letter] = output.get(letter, 0) + 1
    
    return output

try:
    with open('books/frankenstein.txt') as fh:
        text = fh.read()
    
    print(count_words(text))
    print(count_characters(text))
except FileNotFoundError:
    print('''Error: The file frankenstein.txt was not found.''')
