def matrix_multiply(A, B):
    C = [[] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(A[0])):
                sum += A[i][k] * B[k][j]
            C[i].append(sum)
    return C


A = [[0, 1, 2, 3],  [4, 5, 6, 7],  [8, 9, 10, 11]]
B = [[2, 3], [0, 4], [5, -1], [1, 1]]
C = matrix_multiply(A, B)