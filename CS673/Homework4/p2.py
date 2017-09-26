import random
import math


def do():
    n = random.randint(1, 20)
    a = [random.randint(1, 100) for i in range(n)]
    b = [random.randint(1, 100) for i in range(n)]
    a.sort()
    b.sort()
    c = a + b
    c.sort()
    m = int(len(c)/2)
    median = (c[m]+c[m-1])/2
    subArray = check(a, b)
    subArray.sort()
    print("sub array")
    print(subArray)
    m = int(len(subArray)/2)
    print("m=" + str(m))
    actual = (subArray[m]+subArray[m-1])/2
    if median != actual:
        print("fail!!!")
        print(a)
        print(b)
        print(c)
        print(str(median) + " <> " + str(actual))
        return False
    return True


def check(a, b):
    print("subset: A=" + str(a) + ", B=" + str(b))
    print("len(a)=" + str(len(a)) + ", len(b)=" + str(len(b)))
    if len(a) < 3:
        return a + b
    middle = int(len(a) / 2)
    if len(a) % 2 == 1:
        aa = a[middle]
        bb = b[middle]
        if aa >= bb:
            return check(a[0:middle+1], b[middle:len(b)])
        else:
            return check(a[middle:len(a)], b[0:middle+1])
    else:
        aa = (a[middle] + a[middle-1]) / 2
        bb = (b[middle] + b[middle-1]) / 2
        if aa >= bb:
            return check(a[0:middle + 1], b[middle - 1:len(b)])
        else:
            return check(a[middle - 1:len(a)], b[0:middle + 1])


i = 0
while(True):
    i += 1
    if not do():
        print(i)
        break
    print(i)
