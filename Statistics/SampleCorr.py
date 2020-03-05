from Statistics.Covariance import Covariance
from Statistics.StandardDeviation import StandardDeviation
from RandomNumGenerator.NNumFromListSeed import SelectNumbersSeed


class SampleCorrelation:
    @staticmethod
    def correlation(theSeed, dataA, dataB):
        sampleDataA = SelectNumbersSeed.selectNumbers(theSeed, dataA, 5)
        sampleDataB = SelectNumbersSeed.selectNumbers(theSeed, dataB, 5)

        cov = Covariance.covariance(sampleDataA, sampleDataB)
        stdDevA = StandardDeviation.standardDeviation(sampleDataA)
        stdDevB = StandardDeviation.standardDeviation(sampleDataB)
        return cov/(stdDevA*stdDevB)