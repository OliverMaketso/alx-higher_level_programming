#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
   #make a copy of the list my_list
    m_list = my_list.copy()
    # Reverse the copied list
    m_list.reverse()

    for i in m_list:
        print("{}".format(i))

