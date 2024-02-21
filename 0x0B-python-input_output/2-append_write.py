#!/usr/bin/python3
#2-append_write.py

def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)

    Parameters:
    - filename: (str) The name of the file to append to.
    - text: (str) The text content to append to the file.

    Returns:
    - char_count: (int) The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8')as f:
        f.write(text)
        char_count = len(text)

    return(char_count)
