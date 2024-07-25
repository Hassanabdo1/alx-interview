#!/usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
    # Check the input and return an empty list if n <= 0
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    # Use a loop to generate the different rows of Pascal's triangle
    for i in range(1, n):
        # Start the new row with 1
        row = [1]
        # Use a nested loop to generate the middle values of each row
        for j in range(1, i):
            # The middle values are the sum of the two elements above in the previous row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End the new row with 1
        row.append(1)
        # Add the new row to Pascal's triangle
        triangle.append(row)

    return triangle

# Test the function
if __name__ == "__main__":
    """
    0-main
    """
    pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    # Print Pascal's triangle for n = 5
    print_triangle(pascal_triangle(5))

