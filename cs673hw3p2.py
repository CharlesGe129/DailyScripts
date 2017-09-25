import math
import itertools


def nCr(n, r):
    f = math.factorial
    return int(f(n) / f(r) / f(n-r))


def nums(n):
    rs = 0
    for i in range(2, n+1):
        rs += math.factorial(n-1)/(i-1)
    return int(rs)


def all(n):
    allList = []
    [allList.append(list(each)) for each in itertools.permutations([i for i in range(n)])]
    return compare(allList)


def compare(allList):
    rs = 0
    for each in allList:
        num = 1
        best = each[0]
        for i in each:
            if i > best:
                best = i
                num += 1
            if num > 2:
                break
        if num == 2:
            rs += 1
    return rs


for i in range(3, 20):
    print("When n = " + str(i) + ", numbers of permutations with 2 hires is " + str(nums(i)))

