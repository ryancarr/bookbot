def count_words(text:str) -> int:
    """
    This method receives a block of text and counts the number of words returning an integer.
    
    Args:
        text (str): A block of text that needs the words counted.
        
    Returns:
        int: An integer representing the total number of words found in the input text.
    """
    return len(text.split())    

try:
    with open('books/frankenstein.txt') as fh:
        text = fh.read()
    
    print(count_words(text))
except FileNotFoundError:
    print('''Error: The file frankenstein.txt was not found.''')
