import math


def traverse(n, q):
    if q == 0:
        print("With " + str(n) + " soldiers:", end='')
    if n == 3 or n == 4:
        print("Totally " + str(q+1) + " questions")
    else:
        traverse(math.ceil(n/2.0), q+math.floor(n/2.0))


[traverse(i, 0) for i in range(3, 200)]
