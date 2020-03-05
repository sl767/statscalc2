from RandomNumGenerator.SelectSeed import PickSeed
from Statistics.StandardDeviation import StandardDeviation
from Statistics.Mean import Mean

class Z_score:
    @staticmethod
    def z_score(theSeed, data):
        X = PickSeed.pickSeed(theSeed, data)
        mean = Mean.mean(data)
        stdDev = StandardDeviation.standardDeviation(data)
        return (X-mean)/stdDev