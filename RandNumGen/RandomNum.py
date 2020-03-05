import random

class RandomNum:

    @staticmethod
    def random_number(low, high):
        #generates a random integer between two numbers
        #source: https://realpython.com/python-random/

        randomNumber = random.randint(low, high)
        return randomNumber


    @staticmethod
    def random_number_seed(low, high, seed):
        #generates a random integer between two numbers with a seed

        random.seed(seed)
        randomNumber = RandomNum.random_number(low, high)
        return randomNumber