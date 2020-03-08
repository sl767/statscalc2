from RandomNumGenerator.RandPick import RandPick


class PopulationProportion:
    @staticmethod
    def proportion(theSeed, data, rangeNumber):
        subData = RandPick.randPickListSeed(theSeed, data, rangeNumber)
        proportion = len(subData) / len(data)
        return proportion
