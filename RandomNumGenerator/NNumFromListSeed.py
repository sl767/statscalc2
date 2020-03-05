import random
from RandomNumGenerator.NNumFromListNoSeed import SelectNumbersNoSeed


class SelectNumbersSeed:
    @staticmethod
    def selectNumbers(theSeed, aList, rangeNum):
        random.seed(theSeed)

        newList = SelectNumbersNoSeed.selectNumbers(aList, rangeNum)
        return newList
