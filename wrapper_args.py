def outer(times):
    def wrapper(func):
        def inner(*args, **kwargs):
            for i in range(times):
                print(1111)
            return func(*args, **kwargs)

        return inner
    return wrapper


@outer(3)
def test(*args, **kwargs):
    print('test')
    print('args')
    print(type(args))
    [print(each) for each in args]
    print('kwargs')
    print(type(kwargs))
    [print(each) for each in kwargs]
    a = (1, 2, 3)
    print(type(a))
    print(a[2])
    a = [1]
    b = a
    print(a is b)
    b = [1]
    print(a is b)

# test(1, 2, a=3)

a = 1
def test(a):
    a = 2
    print(a)
test(a)
print(a)
