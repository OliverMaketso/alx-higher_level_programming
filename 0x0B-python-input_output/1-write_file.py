#/usr/bin/python3
#1-write_file.py

def write_file(filename="", text=""):
    """
    Writes the given text to a text file (UTF8) 

    Parameters:
    - filename: (str) The name of the file to write to.
    - text: (str) The text content to write to the file.

    Returns:
    - char_count: (int) The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8')as f:
        f.write(text)
        char_count = len(text)

    return(char_count)
