def zero_matrix(M, N):
    matrix = []
    
    for _ in range(M):
        matrix.append([0] * N)
    
    print(matrix)
    return matrix


zero_matrix(10, 10)