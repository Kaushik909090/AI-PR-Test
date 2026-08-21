def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None

    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    if b == 0:
        return None

    return a % b
def square(a):
    return a * a


def average(numbers):
    return sum(numbers) / len(numbers)


def maximum(numbers):
    return max(numbers)

def absolute_difference(a, b):
    return abs(a - b)
def minimum(numbers):
    return min(numbers)
def percentage(a, b):
    return (a / b) * 100
