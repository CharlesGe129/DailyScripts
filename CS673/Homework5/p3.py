S = [0, 1, 2, 4, 5, 7, 11]
D = 20


def f_without_path(i, d):
    if i == 0:
        return S[i]
    if d < 0:
        return 0
    a = f(i-1, d-S[i]) + S[i]
    b = f(i-1, d)
    if a > d and b > d:
        return 0
    elif a > d:
        return b
    elif b > d:
        return a
    else:
        return max(a, b)


A = [[] for i in range(len(S))]


def f_recursion(i, d):
    if i == 0:
        return S[i], [i]
    if d < 0:
        return 0, []
    left, ac = f_recursion(i-1, d-S[i])
    left += S[i]
    if d == D and A[i-1]:
        [right, bc] = A[i-1]
    else:
        right, bc = f_recursion(i - 1, d)
    if d == D:
        if d >= left >= right:
            A[i] = [left, ac + [i]]
        else:
            A[i] = [right, bc]
    if left > d and right > d:
        return 0, []
    elif left > d:
        return right, bc
    elif right > d:
        return left, ac + [i]
    else:
        if left >= right:
            return left, ac + [i]
        else:
            return right, bc


def f():
    matrix = [[0 for j in range(D+1)] for i in range(len(S)+1)]
    path = [[list() for j in range(D+1)] for i in range(len(S)+1)]
    for i in range(1, len(S)):
        for j in range(1, 1+D):
            a = matrix[i-1][j]
            b = matrix[i-1][j-S[i]]+S[i] if j-S[i] >= 0 else 0
            left = 0 if a > j else a
            right = 0 if b > j else b
            matrix[i][j] = max(left, right)
            if left == right == 0:
                pass
            elif left >= right:
                path[i][j] = path[i-1][j]
            elif j-S[i] >= 0:
                path[i][j] = path[i-1][j-S[i]] + [i]


# f_recursion
'''a, b = f_recursion(len(S)-1, D)
print(a)
[print(f"{S[each]}+", end='') for each in b]
print(f"={D}")
[print(each) for each in A]'''

f()
