#!/usr/bin/python3
#0-read_file.py

def read_file(filename=""):
    """Prints the contents of a UTF8 to stdout"""
    with open(filename, encoding="utf-8")as f:
        print(f.read(), end="")
