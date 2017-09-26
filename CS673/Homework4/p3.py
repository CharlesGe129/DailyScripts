import math
import random
import itertools


def limits():
    [print(str(i) + ": " + str(i + math.ceil(math.log(i, 2)) - 2)) for i in range(1, 40)]


def limit(i):
    return i + math.ceil(math.log(i, 2)) - 2


compare = []
num = 0


def cut(A):
    if len(A) == 1:
        return A[0]
    global compare
    global num
    small = []
    for i in range(0, len(A), 2):
        if i+1 >= len(A):
            small.append(A[i])
            continue

        num += 1
        compare[A[i][1]].append(A[i+1])
        compare[A[i+1][1]].append(A[i])
        print("Compare " + str(A[i][0]) + " with " + str(A[i+1][0]))

        if A[i][0] <= A[i+1][0]:
            small.append(A[i])
        else:
            small.append(A[i+1])
    return cut(small)


def find_2(firsts):
    small = firsts[0]
    for i in range(1, len(firsts)):
        if small[0] > firsts[i][0]:
            small = firsts[i]
    return small


def do(A):
    n = len(A)
    global compare
    compare = []
    global num
    num = 0
    for i in range(n):
        compare.append([])
    result = cut(A)
    A.sort()
    aa = []
    for i in range(len(A)):
        aa.append(A[i][0])
    aa.sort()
    print("original: " + str(A))
    print("Sorted: " + str(aa))
    print("Smallest: " + str(result))
    other = compare[result[1]]
    print("Compared to smallest: " + str([each[0] for each in other]))
    second = find_2(other)
    second_other = compare[second[1]]
    print("Compared to second: " + str([each[0] for each in second_other]))
    actual = num + len(other) - 1
    print("Actual: " + str(actual))
    expect = n + math.ceil(math.log(n, 2)) - 2
    print("Expect: " + str(expect))
    third = [each[0] for each in second_other]
    third.extend([each[0] for each in other])
    n = len(third)
    old = len(other) + len(third) - 3
    new = limit(len(third))
    print("old: " + str(old))
    print("new: " + str(new))
    print()
    return old <= new


def check_all():
    for n in range(10, 15):
        all = [list(each) for each in itertools.permutations([i for i in range(1, n)])]
        for each in all:
            print(n)
            A = []
            for i in range(len(each)):
                A.append([each[i], i])
            if not do(A):
                print("fail!!!!!!!")
                break
        break

check_all()
