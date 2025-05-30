#!/usr/bin/python3
'''
This is the "5-text_indentation" module.
The example module supplies one function, def text_indentation().
'''


def text_indentation(text):
    '''
    function that prints a text with 2 new lines after these
    characters: ., ? and :
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, char + "\n\n")

    print("\n".join(line.strip() for line in text.split("\n")), end="")
