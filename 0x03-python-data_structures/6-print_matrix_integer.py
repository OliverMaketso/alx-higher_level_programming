#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            # Use str.format() to print each integer with formatting
            if i == len(row) - 1:
                # If it's the last element in the row, end with a new line
                print("{:d}".format(num))
            else:
                # If it's not the last element, separate with a space
                print("{:d}".format(num), end=" ")
    if not matrix:
        print()  # Print an empty line if the matrix is empty
