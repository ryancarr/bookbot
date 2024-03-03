'''Main entry point of program

Args:
    None
    
Returns:
    None
'''
def main():
    path = f'books/frankenstein.txt'
    text = get_book_text(path)
    words = count_words(text)
    letter_count = count_letters(text)
    letters = letters_dict_to_sorted_list(letter_count)
    print_report(path, words, letters)


'''Counts the number of words in the book

Args:
    text (str): complete contents of the book
    
Returns:
    int: Number of words in the book, split on spaces
'''
def count_words(text: str) -> int:
    words = text.split()
    return len(words)


'''Counts the number of letters in the book

Args:
    text (str): complete contents of the book
    
Returns:
    dict: Dictionary of letter, count pairs
'''
def count_letters(text: str) -> dict:
    letters = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            letters[letter] = letters.get(letter, 0) + 1
    return letters


'''Returns a string containing the full contents of the book

Args:
    path (str): path to book we're examining
    
Returns:
    str: A string containing the full contents of the book
'''
def get_book_text(path: str) -> str:
    with open(path) as fh:
        text = fh.read()
    return text


'''Prints a report of the book statistics

Args:
    path (str)    : path to book we're examining
    words (int)   : quantity of words in the book
    letters (list): sorted list of all the letters and their frequency

Returns:
    None
'''
def print_report(path: str, words: int, letters: list) -> None:
    print(f'--- Begin report of {path} ---')
    print(f'{words} words found in the document\n')
    for letter in letters:
        print(f'The \'{letter["letter"]}\' character was found {letter["num"]} times')
    print(f'--- End report ---')


'''Returns a sorted list of letters in descending frequency order

Args:
    dict: A dictionary of letter, count pairs

Returns:
    list: A sorted list of dictionaries containing the keys letter and num
'''
def letters_dict_to_sorted_list(letter_count: dict) -> list:
    # Build a list of dictionaries separating letter and count into separt k,v pairs
    letters = [{'letter':letter, 'num':count} for letter, count in letter_count.items()]
    
    # Sort the list using a custom function ensuring it is sorted by 'num' values
    letters.sort(reverse=True, key=sort_on)
    return letters


'''Function for custom sorting of letters dictionary based on nums key

Args:
    dict (dict): Dictionary containing num key

Returns:
    int: A number representing the quantity of the current letter
'''
def sort_on(dict: dict):
    return dict['num']

# Entry point
main()