import unittest
from numpy.random import seed
from numpy.random import randint
from pprint import pprint

from Statistics.Mean import Mean
from Statistics.Median import Median
from Statistics.MeanDeviation import MeanDeviation
from Statistics.Mode import Mode
from Statistics.Quartiles import Quartile
from Statistics.Skewness import Skewness
from Statistics.StandardDeviation import StandardDeviation
from Statistics.Variance import Variance
from Statistics.Zscore import Z_score
from Statistics.Covariance import Covariance
from Statistics.PopCorr import PopCorrelation
from Statistics.SampleCorr import SampleCorrelation
from Statistics.PopProportion import PopulationProportion


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(5)
        self.testData = randint(0, 50, 15)
        self.testData2 = randint(1, 51, 15)

    def test_mean(self):
        mean = Mean.mean(self.testData)
        self.assertEqual(mean, 25.466666666666665)

    def test_median(self):
        median = Median.median(self.testData)
        self.assertEqual(median, 27.0)

    def test_standardDeviation(self):
        standardDeviation = StandardDeviation.standardDeviation(self.testData)
        self.assertEqual(standardDeviation, 14.01364414498321)

    def test_variance(self):
        variance = Variance.variance(self.testData)
        self.assertEqual(variance, 196.3822222222222)

    def test_mode(self):
        mode = Mode.mode(self.testData)
        self.assertEqual(mode, 16)

    def test_meanDeviation(self):
        meanDeviation = MeanDeviation.meanDeviation(self.testData)
        self.assertEqual(meanDeviation, 12.835555555555555)

    def test_quartiles(self):
        quartiles = Quartile.quartile(self.testData)
        self.assertEqual(quartiles, (13.0, 27.0, 37.0))

    def test_skewness(self):
        skewness = Skewness.skewness(self.testData)
        self.assertEqual(skewness, 0.15182604770872699)

    def test_z_score(self):
        z_score = Z_score.z_score(2, self.testData)
        self.assertEqual(z_score, -1.3177633508895406)

    def test_covariance(self):
        covariance = Covariance.covariance(self.testData, self.testData2)
        self.assertEqual(covariance, -19.961904761904755)

    def test_popCorrelation(self):
        result = PopCorrelation.correlation(self.testData, self.testData2)
        self.assertEqual(result, -0.09958703367427517)

    def test_sampleCorrelation(self):
        result = SampleCorrelation.correlation(3, self.testData, self.testData2)
        self.assertEqual(result, -0.5940762068478092)

    def test_population_Proportion(self):
        result = PopulationProportion.proportion(3, self.testData, 4)
        self.assertEqual(result, 0.26666666666666666)


if __name__ == '__main__':
    unittest.main()
