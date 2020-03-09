from Calculator.Square import squaring
from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Statistics.Zscore import Z_score
from PopSampling.MarginOfErr import MarginError

class UnknownPop:
    @staticmethod
    def unknown_pop_sample(seed, data, percent):

        z_s = Z_score.z_score(seed, data)
        m_e = MarginError.margin(seed, data)
        p = percent
        q = subtraction(1, p)

        val = division(z_s, m_e)
        samplePop = squaring(val) * p * q

        return samplePop