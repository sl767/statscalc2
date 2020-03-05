from numpy.random import seed
import random


class RandomList():
    @staticmethod
    def list_Of_Ints(num1, num2, length, theSeed):
        if isinstance(num1, float):
            return listFloats(num1, num2, length, theSeed)

        aList = []
        seed(theSeed)

        for each in range(length):
            number = random.randint(num1, num2)
            aList.append(number)

        return aList

    @staticmethod
    def list_Of_Floats(num1, num2, length, theSeed):
        aList = []
        seed(theSeed)

        for each in range(length):
            number = random.uniform(num1, num2)
            aList.append(number)

        return aList