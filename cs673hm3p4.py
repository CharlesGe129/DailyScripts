import random
import itertools

aa = 0


def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            a = array[i]
            array[i] = array[j]
            array[j] = a
    a = array[i+1]
    array[i+1] = array[r]
    array[r] = a
    return i + 1


def quick_sort(array, p, r):
    global aa
    aa += 1
    while p < r:
        q = partition(array, p, r)
        if q == p:
            p = q + 1
        elif q == r:
            r = r - 1
        else:
            quick_sort(array, p, q - 1)
            p = q + 1


def check_worst_case(n):
    global aa
    all = [list(each) for each in itertools.permutations([i for i in range(1, n)])]
    max = 0
    for each in all:
        quick_sort(each, 0, len(each)-1)
        if aa > max:
            max = aa
        aa = 0
    print(str(n) + ': ' + str(max))


#[check_worst_case(i) for i in range(2, 12)]
a = [1, 2, 3, 4, 5, 6, 7]
quick_sort(a, 0, 6)
print(aa)