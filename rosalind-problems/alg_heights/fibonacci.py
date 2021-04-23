def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num-1)+fibonacci(num-2)


def fib_loop(num):
    old = 1
    new = 1
    for _ in range(num - 1):
        tmp_val = new
        new = old
        old = old + tmp_val
    return new


def pythonic_fib_loop(num):
    old, new = 1, 1
    for _ in range(num - 1):
        new, old = old, old + new
    return new
