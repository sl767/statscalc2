import random


class RandNoSeed:
    @staticmethod
    def randInt(num1, num2):
        if isinstance(num1, float):
            return RandNoSeed.randFloat(num1, num2)
        return random.randint(num1, num2)

    @staticmethod
    def randFloat(num1, num2):
        return random.uniform(num1, num2)