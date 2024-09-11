def rotate_2d_matrix(matrix):
    # Transpose the matrix (swap rows with columns)
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the 90 degree rotation
    for i in range(n):
        matrix[i].reverse()

