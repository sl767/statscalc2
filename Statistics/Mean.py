from Calculator.Calculator import Addition
from Calculator.Calculator import Division


def mean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = Addition(total, num)
    return Division(total, num_values)
