import copy
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
result = copy.deepcopy(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            
