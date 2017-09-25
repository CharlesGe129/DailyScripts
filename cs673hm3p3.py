import math
import itertools


def do(n, times):
    if n <= 1:
        return times
    n -= 1
    times += 1
    a = math.floor(n-1)
    times = do(a, times)
    return times


[print("When N=" + str(i) + ", the smallest possible times is " + str(do(i, 0))) for i in range(6, 40)]