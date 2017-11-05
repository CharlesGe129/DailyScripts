import random


def solution(matrix):
    potential = find_potential(matrix)
    print(potential)
    result = check_potential(matrix, potential)
    print(result)


def find_potential(matrix):
    i = 0
    j = 0
    n = len(matrix)
    while True:
        if matrix[i][j] == 0 and j < n - 1:
            j += 1
        elif matrix[i][j] == 1 and i < n - 1:
            i += 1
        else:
            break
    return i


def check_potential(matrix, potential):
    for i in range(len(matrix)):
        if matrix[potential][i] != 0:
            return False
        if matrix[i][potential] != 1 and i != potential:
            return False
    return True


def format_matrix(n, u):
    m = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(0, 1))
        m.append(row)
    for i in range(n):
        m[i][u] = 1
        m[u][i] = 0
    for i in range(n):
        for j in range(n):
            print(f"{m[i][j]} ", end='')
        print()
    return m

solution(format_matrix(10, 5))
