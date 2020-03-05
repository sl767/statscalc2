from numpy.random import seed
import random


class RandomList:
    @staticmethod
    def listOfInts(num1, num2, length, theSeed):
        if isinstance(num1, float):
            return listOfFloats(num1, num2, length, theSeed)

        aList = []
        seed(theSeed)

        for each in range(length):
            number = random.randint(num1, num2)
            aList.append(number)

        return aList

    @staticmethod
    def listOfFloats(num1, num2, length, theSeed):
        aList = []
        seed(theSeed)

        for each in range(length):
            number = random.uniform(num1, num2)
            aList.append(number)

        return aList