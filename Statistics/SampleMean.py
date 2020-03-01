from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.division import Division
from Statistics.Getsample import getSample


def sample_mean(data, sample_size):
    total = 0

    sample = getSample(data, sample_size)
    num_values = len(sample)
    for num in sample:
        total = Addition(total, num)
    return Division(total, num_values)
