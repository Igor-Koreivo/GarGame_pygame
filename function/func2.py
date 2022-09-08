def func1():
    x = 'x1'
    return x


def func2(y):
    z = 'x2'
    return y, z


print(func2(func1()))