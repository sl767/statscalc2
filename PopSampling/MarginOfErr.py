from Statistics.StandardDeviation import StandardDeviation
from Statistics.Zscore import Z_score
from Calculator.Multiplication import multiplication


class MarginError:
    @staticmethod
    def margin(seed, data):
        zs= Z_score.z_score(seed, data)
        sd = StandardDeviation.standardDeviation(data)
        margin = multiplication(zs, sd)
        return margin