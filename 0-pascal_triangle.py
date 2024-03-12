#!/usr/bin/python3
def pascal_triangle(n):
    # Checks if the input list is <= 0
    if n <= 0:
        return []
    # Stores the rows of the Pascal triangle
    pascal_triangle = []
    for i in range(n):
        pascal_row = [1]
        # Checks if the current index is greater than 0
        if i > 0:
            # Accesses the previous row of the triangle list
            prev_row = pascal_triangle[i-1]
            # Iterate within the first and last element
            for j in range(1, i):
                pascal_row.append(prev_row[j-1] + prev_row[j])
            # We append (add) 1 to the end of the row
            pascal_row.append(1)
        pascal_triangle.append(pascal_row)
    return pascal_triangle
