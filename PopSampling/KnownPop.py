from Calculator.SquareRoot import squareRoot
from Statistics.Zscore import Z_score
from Statistics.StandardDeviation import StandardDeviation
from PopSampling.MarginOfErr import MarginError


class KnownPop:
    @staticmethod
    def known_pop_sample(seed, data):
        z_s = Z_score.z_score(seed, data)
        m_e = MarginError.margin(seed, data)
        s_d = StandardDeviation.standardDeviation(data)

        value = (z_s * s_d) / m_e

        popSample = squareRoot(value)

        return popSample
