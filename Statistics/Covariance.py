import numpy


class Covariance:
    @staticmethod
    def covariance(data1, data2):
        return numpy.cov(data1, data2)[0,1]