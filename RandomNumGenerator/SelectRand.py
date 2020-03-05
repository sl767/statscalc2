import random


class SelectRandomly:
    @staticmethod
    def pick(aList):
        listLen = len(aList)
        position = random.randint(0, listLen-1)
        return aList[position]
