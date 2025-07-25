# inc.py
# Your main function under test

import math
def inc(x):
    return x + 1



def dec(x):
    return x - 1


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def mod(x, y):
    return x % y


def pow(x, y):
    return x ** y


def sqrt(x):
    return x ** 0.5



def log(x):
    return math.log(x)


def exp(x):
    return math.exp(x)


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def tan(x):
    return math.tan(x)


def cot(x):
    return 1 / math.tan(x)


def log10(x):
    return math.log10(x)


def log2(x):
    return math.log2(x)


def factorial(x):
    return math.factorial(x)


def fibonacci(x):
    return math.fibonacci(x)


def is_even(x):
    return x % 2 == 0


def is_odd(x):
    return x % 2 != 0


def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True


def is_palindrome(x):
    return str(x) == str(x)[::-1]


def is_even(x):
    return x % 2 == 0


def is_odd(x):
    return x % 2 != 0


def is_prime(x):
    if x <= 1:
        return False