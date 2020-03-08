from RandomNumGenerator.RandPick import RandPick
from Statistics.StandardDeviation import StandardDeviation
from Statistics.Mean import Mean


class Z_score:
    @staticmethod
    def z_score(seed, data):
        X = RandPick.randPickSeed(seed, data)
        mean = Mean.mean(data)
        stdDev = StandardDeviation.standardDeviation(data)
        return (X - mean) / stdDev
