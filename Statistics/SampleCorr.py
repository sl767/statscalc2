from Statistics.Covariance import Covariance
from Statistics.StandardDeviation import StandardDeviation
from RandomNumGenerator.RandPick import RandPick


class SampleCorrelation:
    @staticmethod
    def correlation(theSeed, dataA, dataB):
        sampleDataA = RandPick.randPickListSeed(theSeed, dataA, 5)
        sampleDataB = RandPick.randPickListSeed(theSeed, dataB, 5)

        cov = Covariance.covariance(sampleDataA, sampleDataB)
        stdDevA = StandardDeviation.standardDeviation(sampleDataA)
        stdDevB = StandardDeviation.standardDeviation(sampleDataB)
        return cov/(stdDevA*stdDevB)