import random
from RandNumGen.Random import PickRandomly

class PickSeed():
    @staticmethod
    def pickSeed(theSeed, aList):
        random.seed(theSeed)

        return PickRandomly.pick(aList)