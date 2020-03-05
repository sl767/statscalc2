import random
from RandomNumGenerator.SelectRand import SelectRandomly

class PickSeed:
    @staticmethod
    def pickSeed(theSeed, aList):
        random.seed(theSeed)

        return SelectRandomly.pick(aList)