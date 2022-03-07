from typing import List

import numpy as np
import matplotlib.pyplot as plt

from tournesol import Tournesol


class Field:
    def __init__(self, seedPattern):
        self.tournesols: List[List[Tournesol]] = []
        self._createTournesols(seedPattern)

        self.size = seedPattern.shape

        self._ambientLight = 0.2
        self._sunlightCompetitionFactor = 3
        self._resourceCompetitionFactor = 2

    def nextDay(self):
        # Write code here
        raise NotImplementedError()

    def getHeightMap(self):
        # Write code here
        raise NotImplementedError()

    def getHeightAt(self, x, y):
        if y < 0 or y >= self.size[0]:
            return 0
        if x < 0 or x >= self.size[1]:
            return 0
        if self.tournesols[y][x] is None:
            return 0
        return self.tournesols[y][x].height

    def showHeightMap(self):
        heightMap = self.getHeightMap()

        plt.imshow(heightMap)
        plt.show()

    def _createTournesols(self, seedPattern: np.ndarray):
        self.tournesols: List[List[Tournesol]] = []
        for seedRow in seedPattern:
            tournesolRow = []
            for seed in seedRow:
                if seed == 1.0:
                    tournesolRow.append(Tournesol())
                else:
                    tournesolRow.append(None)
            self.tournesols.append(tournesolRow)

    def _getSunlightAt(self, x, y):
        if y == 0:
            return 1
        neighborsCoords = [(x-1, y-1), (x, y-1), (x+1, y-1)]
        neighborsHeights = [self.getHeightAt(x, y) for (x, y) in neighborsCoords]

        shadowFactor = self._getShadowFactor(*neighborsHeights)
        if shadowFactor == 0:
            return 1

        directLight = self.tournesols[y][x].height / shadowFactor / self._sunlightCompetitionFactor

        return min(1, (1-self._ambientLight)*directLight + self._ambientLight)

    def _getResourcesAt(self, x, y):
        neighborsCoords = [(x, y-1), (x, y+1), (x+1, y), (x-1, y)]
        neighborsHeights = [self.getHeightAt(x, y) for (x, y) in neighborsCoords]
        heightFactor = sum(neighborsHeights) / 4
        if heightFactor == 0:
            return 1
        resources = self.tournesols[y][x].height / heightFactor / self._resourceCompetitionFactor
        return min(1, resources)

    def _getShadowFactor(self, h1, h2, h3):
        return 0.25*h1 + 0.5*h2 + 0.25*h3
