import random

class SelectNumbersNoSeed():
    @staticmethod
    def selectNumbers(aList, rangeNum):
        newList =[]
        listSize = len(aList)

        for each in range(rangeNum):
            position = random.randint(0, listSize-1)
            newList.append(aList[position])

        return newList