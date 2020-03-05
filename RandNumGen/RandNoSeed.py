import random


class RandomNoSeed():
    @staticmethod
    def randomInt(num1, num2):
        if isinstance(num1, float):
            return RandomNoSeed.randomFloat(num1, num2)
        return random.randint(num1, num2)

    @staticmethod
    def randomFloat(num1, num2):
        return random.uniform(num1, num2)