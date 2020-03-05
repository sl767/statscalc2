from RandomNumGenerator.NNumFromListSeed import SelectNumbersSeed


class PopulationProportion:
    @staticmethod
    def proportion(theSeed, data, rangeNumber):
        subData = SelectNumbersSeed.pickNumbers(theSeed, data, rangeNumber)
        proportion = len(subData) / len(data)
        return proportion
