import numpy


class Quartile:
    @staticmethod
    def quartile(data):
        q1 = numpy.quantile(data, .25)
        q2 = numpy.quantile(data, .50)
        q3 = numpy.quantile(data, .75)
        return q1, q2, q3
