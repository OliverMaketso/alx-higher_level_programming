#!/usr/bin/python3
# 1-my_list.py

class MyList(list):
    def print_sorted(self):
        """
        Prints the list in sorted order (ascending sort).
        """
        sorted_list = sorted(self)
        print(sorted_list)

