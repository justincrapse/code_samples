

def fibonacci(iterations):
    a, b = 0, 1
    for i in range(iterations):
        yield a
        a, b = a + b, a


print(list(fibonacci(15)))
