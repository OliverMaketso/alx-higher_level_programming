#!/usr/bin/python3
# 3-is_kind_of_class.py

def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class.

    Parameters:
    obj (object): The object to check.
    a_class (class): The class to compare against.

    Returns:
    bool: True if the object is an instance of the specified class or its subclass; otherwise False.
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)

