import random
import itertools

aa = 0


def partition(array, p, r):
    global aa
    aa += 1
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


def quick_sort(array, p, q):
    if p < q:
        index = partition(array, p, q)
        quick_sort(array, p, index-1)
        quick_sort(array, index+1, q)


def check_worst_case(n):
    global aa
    all = [list(each) for each in itertools.permutations([i for i in range(1, n)])]
    min = 99
    for each in all:
        quick_sort(each, 0, len(each)-1)
        if aa < min:
            min = aa
        aa = 0
    print(str(n-1) + ': ' + str(min))


size = random.randint(1, 50)
array = [random.randint(0, 100) for i in range(size)]
array = [8, 7, 6, 1, 4, 3, 2, 5]
quick_sort(array, 0, len(array)-1)
print(aa)


[check_worst_case(i) for i in range(1, 12)]
