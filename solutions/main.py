import seedPatterns
from field import Field

import numpy as np
import matplotlib.pyplot as plt


meanHeightMap = np.zeros((20, 20))
N = 100
days = 100
for j in range(N):
    field = Field(seedPattern=seedPatterns.random90())
    for i in range(days):
        # field.showHeightMap()
        field.nextDay()
    heightMap = field.getHeightMap()
    meanHeightMap += heightMap

meanHeightMap /= N

plt.imshow(meanHeightMap)
plt.show()
