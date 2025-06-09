def pascal_triangle(n):
    """Calculate Pascal's Triangle up to n rows."""
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev_row = triangle[-1]
            row = [1]  # start with 1
            # sum of adjacent elements in the previous row
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # end with 1
            triangle.append(row)
    return triangle
