import random


class Tournesol:
    def __init__(self):
        self.height = 0.05
        self.branches = 0

    def grow(self, sunlight: float, resources: float):
        if (sunlight + resources)/2 > random.uniform(0, 1):
            if random.uniform(0, 1) > 0.2:
                self._growBranch()
            else:
                self._growHigher()

    def _growBranch(self):
        self.branches += 1

    def _growHigher(self):
        self.height += random.gauss(0.01 + self.branches * 0.002, 0.002)
