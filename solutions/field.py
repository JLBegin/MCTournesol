from typing import List

import numpy as np
import matplotlib.pyplot as plt

from tournesol import Tournesol


class Field:
    def __init__(self, seedPattern):
        self.tournesols: List[List[Tournesol]] = []
        self.size = seedPattern.shape

        self._createTournesols(seedPattern)

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

    def nextDay(self):
        for y, tournesolRow in enumerate(self.tournesols):
            for x, tournesol in enumerate(tournesolRow):
                if tournesol is None:
                    continue
                tournesol.grow(self._getSunlightAt(x, y), self._getResourcesAt(x, y))

    def _getSunlightAt(self, x, y):
        if y == 0:
            return 1
        neighborsCoords = [(x-1, y-1), (x, y-1), (x+1, y-1)]
        neighborsHeights = [self.getHeightAt(x, y) for (x, y) in neighborsCoords]

        shadowFactor = self._getShadowFactor(*neighborsHeights)
        if shadowFactor == 0:
            return 1

        directLight = self.tournesols[y][x].height / shadowFactor / 3
        ambientLight = 0.2

        return min(1, (1-ambientLight)*directLight + ambientLight)

    def _getResourcesAt(self, x, y):
        neighborsCoords = [(x, y-1), (x, y+1), (x+1, y), (x-1, y)]
        neighborsHeights = [self.getHeightAt(x, y) for (x, y) in neighborsCoords]
        heightFactor = sum(neighborsHeights) / 4
        if heightFactor == 0:
            return 1
        resources = self.tournesols[y][x].height / heightFactor / 2
        return min(1, resources)

    def getHeightAt(self, x, y):
        if y < 0 or y >= self.size[0]:
            return 0
        if x < 0 or x >= self.size[1]:
            return 0
        if self.tournesols[y][x] is None:
            return 0
        return self.tournesols[y][x].height

    def _getShadowFactor(self, h1, h2, h3):
        return 0.25*h1 + 0.5*h2 + 0.25*h3

    def showHeightMap(self):
        heightMap = self.getHeightMap()

        plt.imshow(heightMap)
        plt.show()

    def getHeightMap(self):
        heightMap = np.zeros(self.size)
        for y, tournesolRow in enumerate(self.tournesols):
            for x, tournesol in enumerate(tournesolRow):
                if tournesol is None:
                    heightMap[y, x] = 0
                    continue
                heightMap[y, x] = tournesol.height
        return heightMap
