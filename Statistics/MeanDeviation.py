import numpy


class MeanDeviation:
    @staticmethod
    def meanDeviation(data):
        return numpy.mean(numpy.absolute(data - numpy.mean(data)))
    