from scipy.stats import sem
from scipy.stats import t
from PopSampling.ConfidenceIntPop import ConfidenceIntPop
from PopSampling.RandomSample import RandomSample

class ConfidenceIntSamp:
    @staticmethod
    def confidenceInt(confidence, data, seed, high):
        data = RandomSample.random_sample(seed, data, high)
        cip = ConfidenceIntPop.confidence_interval(confidence, data)
        return cip