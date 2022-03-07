import random


class Tournesol:
    def __init__(self):
        self.height = 0.05
        self.branches = 0

    def grow(self, sunlight: float, resources: float):
        # Write code here
        raise NotImplementedError()

    def _growBranch(self):
        self.branches += 1

    def _growHigher(self):
        self.height += random.gauss(0.01 + self.branches * 0.002, 0.002)
