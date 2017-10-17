S = [1, 2, 4, 5, 20, 3]
D = 11


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


def f(i, d):
    if i == 0:
        return S[i], [i]
    if d < 0:
        return 0, []
    left, ac = f(i-1, d-S[i])
    left += S[i]
    if d == D and A[i-1]:
        [right, bc] = A[i-1]
    else:
        right, bc = f(i - 1, d)
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


a, b = f(len(S)-1, D)
print(a)
[print(f"{S[each]}+", end='') for each in b]
print(f"={D}")
[print(each) for each in A]