from CS333.lab12 import iterate


def s1(a, b, c):
    return c


def s2(a, b, c):
    return 0.5 * a


def s3(a, b, c):
    return 0.5*a + b


if __name__ == '__main__':
    iterate(5, 0, [s1, s2, s3])
