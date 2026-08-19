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


def average(numbers):
    if not numbers:
        return None

    return sum(numbers) / len(numbers)


def maximum(numbers):
    if not numbers:
        return None

    return max(numbers)

def absolute_difference(a, b):
    return abs(a - b)
def minimum(numbers):
    if not numbers:
        return None

    return min(numbers)
