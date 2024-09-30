def pascal_triangle(n: int) -> list[list[int]]:
    if n < 1:
        return []
    triangle = [[1], [1, 1]]
    for i in range(2, n):
        row = [0] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        row[0] = row[-1] = 1
        triangle.append(row)
    return triangle[:n]
