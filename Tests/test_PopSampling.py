import unittest
from numpy.random import seed
from numpy.random import randint
from pprint import pprint

from PopSampling.Cochrans import Cochran
from PopSampling.ConfidenceIntPop import ConfidenceIntPop
from PopSampling.ConfidenceIntSamp import ConfidenceIntSamp
from PopSampling.KnownPop import KnownPop
from PopSampling.MarginOfErr import MarginError
from PopSampling.RandomSamp import SimpleRandSamp
from PopSampling.SystemicSamp import SysSamp
from PopSampling.UnknownPop import UnknownPop

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        seed(seed=3)
        self.testData = randint(low=0, high=50, size=15)

    def test_RandomSample(self):
        sample = SimpleRandSamp.simpleRandSamp(seed=3, data=self.testData, lstLen=5)
        self.assertEqual(sample, [8, 41, 43, 3, 21])

    def test_SystematicSample(self):
        result = SysSamp.sysSamp(aLst=self.testData)
        self.assertEqual(result, [3, 21, 43, 21, 20])

    def test_ConfidenceIntPop(self):
        result = ConfidenceIntPop.confidence_interval(confidence=.90, data=self.testData)
        self.assertEqual(result, (15.581632402905116, 28.68503426376155))

    def test_ConfidenceIntSamp(self):
        result = ConfidenceIntSamp.confidenceInt(confidence=.90, data=self.testData, seed=3, high=5)
        self.assertEqual(result, (5.6669372302865675, 40.73306276971343))

    def test_MarginError(self):
        result = MarginError.margin(data=self.testData, seed=3)
        self.assertEqual(result, -14.133333333333335)

    def test_Cochran(self):
        result = Cochran.cochran(data=self.testData, lstLen=4, seed=3)
        self.assertEqual(result, 0.0010094984628091588)

    def test_UnknownPopulation(self):
        result = UnknownPop.unknown_pop_sample(data=self.testData, seed=3, percent=0.41)
        self.assertEqual(result, 0.0012487381269214882)

    def test_KnownPopulation(self):
        result = KnownPop.known_pop_sample(data=self.testData, seed=3)
        self.assertEqual(result, 1.0)


if __name__ == '__main__':
    unittest.main()