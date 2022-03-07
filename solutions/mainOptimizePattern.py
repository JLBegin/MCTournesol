from field import Field
import seedPatterns

import numpy as np
import matplotlib.pyplot as plt


patterns = [seedPatterns.vertical, seedPatterns.horizontal, seedPatterns.grid]

for pattern in patterns:
    meanHeightMap = np.zeros((20, 20))
    N = 100
    days = 100
    for j in range(N):
        field = Field(seedPattern=pattern)
        for i in range(days):
            # field.showHeightMap()
            field.nextDay()
        heightMap = field.getHeightMap()
        meanHeightMap += heightMap
    meanHeightMap /= N

    plt.imshow(meanHeightMap)
    plt.show()
    print(np.sum(meanHeightMap) / 200)
