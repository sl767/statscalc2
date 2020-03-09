from RandomNumGenerator.RandPick import RandPick


class SysSamp(RandPick):

    def sysSamp(self, seed, nums, data):
        return self.randPickListSeed(seed, nums, data)