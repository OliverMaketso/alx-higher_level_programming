#!/usr/bin/python3
#0-lookup.py
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    
    Parameters:
    obj (object): The object to inspect.
    
    Returns:
    list: A list containing the names of attributes and methods.
    """
    # Get all attributes and methods of the object
    attributes_and_methods = dir(obj)
    
    # Filter out private attributes and methods (those starting with '__')
    public_attributes_and_methods = [attr for attr in attributes_and_methods if not attr.startswith('__')]
    
    return public_attributes_and_methods

obj = Example()
print(lookup(obj))

