import random


def do(a):
    [swap(a, i, random.randint(i+1, len(a)-1)) for i in range(len(a)-1)]


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def check_all_output():
    aa = set()
    for i in range(999):
        a = ['1', '2', '3', '4']
        do(a)
        aa.add(', '.join(a))

    print(aa)
    print(len(aa))

check_all_output()