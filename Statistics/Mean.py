from Calculator.Division import division
from Calculator.Addition import addition


def mean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = addition(total, num)
    return division(total, num_values)
