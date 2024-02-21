#/usr/bin/python3
#4-from_json_string.py

import json
def from_json_string(my_str):
    """
    Returns the Python data structure represented by the given JSON string.

    Parameters:
    - my_str: (str) The JSON string to be converted to a Python data structure.

    Returns:
    - python_obj: The Python data structure represented by the JSON string.
    """
    # Use the json.loads() function to parse the JSON string and convert it to a Python object
    python_obj = json.loads(my_str)

    # Return the Python object
    return(python_obj)
