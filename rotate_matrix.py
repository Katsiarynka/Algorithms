def rotate(A):
    if not A:
        return A
    n, m = len(A), len(A[0])
    rotatedA = []
    for i in range(m):
        rotatedA.append([0] * n)

    for i in range(n):
        for j in range(m):
            rotatedA[j][n - i - 1] = A[i][j]
    return rotatedA


assert(rotate([[1, 2, 3, 4],[3,4, 5, 6], [5, 6, 7, 8]]) == [[5, 3, 1], [6, 4, 2], [7, 5, 3], [8, 6, 4]])
