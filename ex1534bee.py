import random
user_array = int(input())
for i in range(user_array):
    sequence = (random.randint(1, 3)for _ in range(user_array))


import sys

def create_matrix(N):
    matrix = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                matrix[i][j] = 1
            elif i + j == N - 1:
                matrix[i][j] = 2
            elif j > i and i + j < N - 1:
                matrix[i][j] = 3
            elif i > j and i + j < N - 1:
                matrix[i][j] = 3
            elif i < j and i + j > N - 1:
                matrix[i][j] = 3
            elif i > j and i + j > N - 1:
                matrix[i][j] = 3
            else:
                matrix[i][j] = 4
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print("".join(map(str, row)))

for line in sys.stdin:
    N = int(line.strip())
    if 3 <= N < 70:
        matrix = create_matrix(N)
        print_matrix(matrix)
        print()
