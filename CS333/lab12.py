def iterate(times, tax, funcs):
    (a, b, c) = (1, 1, 1)
    fac = 1 - tax
    for i in range(times):
        a1 = fac*funcs[0](a, b, c) + tax
        b1 = fac*funcs[1](a, b, c) + tax
        c1 = fac*funcs[2](a, b, c) + tax
        (a, b, c) = (a1, b1, c1)
        print(f"#{i+1}: a={a}, b={b}, c={c}")


def s1(a, b, c):
    return c


def s2(a, b, c):
    return 0.5 * a


def s3(a, b, c):
    return 0.5*a + b

if __name__ == '__main__':
    iterate(5, 0.15, [s1, s2, s3])
