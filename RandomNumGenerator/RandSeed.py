import random
from random import seed


class RandSeed:
    @staticmethod
    def randomInt(theSeed, num1, num2):
        random.seed(theSeed)
        if isinstance(num1, float):
            return RandSeed.randomFloat(theSeed, num1, num2)
        return random.randint(num1, num2)

    @staticmethod
    def randomFloat(theSeed, num1, num2):
        random.seed(theSeed)
        ranNum = random.uniform(num1, num2)
        return ranNum


'''
    seed(5)
    self.testData = randint(0, 10, 20)
    pprint.pprint(self.testData)
    self.statistics = Statistics()
'''
print(RandSeed.randomInt(5, 1, 20))
print(RandSeed.randomInt(2, 2.3, 9.9))
