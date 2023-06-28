def solution(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_sum = 0

    for j in range(cols):
        for i in range(rows):
            if matrix[i][j] == 0:
                break
            total_sum += matrix[i][j]

    return total_sum

matrix1 = [[0, 1, 1, 2], 
           [0, 5, 0, 0], 
           [2, 0, 3, 3]]
print(solution(matrix1))

matrix2 = [[1, 1, 1, 0], 
           [0, 5, 0, 1], 
           [2, 1, 3, 10]]
print(solution(matrix2))