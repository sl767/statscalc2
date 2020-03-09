from Statistics.Zscore import Z_score
from PopSampling.MarginOfErr import MarginError
from Statistics.PopProportion import PopulationProportion
from Calculator.Exponentiation import exponentiation
from Calculator.Subtraction import subtraction


class Cochran:
    @staticmethod
    def cochran(seed, lstLen, data):
        z_s = Z_score.z_score(seed, data)
        p_p = PopulationProportion.proportion(seed, lstLen, data)
        m_e = MarginError.margin(seed, data)
        q = subtraction(1, p_p)

        cochransamp = (exponentiation(z_s, 2) * p_p * q) / exponentiation(m_e, 2)

        return cochransamp
