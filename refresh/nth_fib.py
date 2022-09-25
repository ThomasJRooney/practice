def getNthFib(n):
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a
