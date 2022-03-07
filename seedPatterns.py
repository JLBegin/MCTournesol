import numpy as np


horizontal = np.ones((20, 20))
for i in range(20):
    if i % 2 == 0:
        horizontal[i] = np.zeros(20)

grid = np.ones((20, 20))
for i in range(20):
    for j in range(20):
        if (i + j) % 2 == 0:
            grid[i, j] = 0

vertical = np.ones((20, 20))
for i in range(20):
    if i % 2 == 0:
        vertical[:, i] = np.zeros(20)


def random90():
    field = np.ones((20, 20))
    for index in np.random.choice(np.arange(0, 20*20), size=40, replace=False):
        x, y, = index // 20, index % 20
        field[y, x] = 0
    return field


def random50():
    field = np.ones((20, 20))
    for index in np.random.choice(np.arange(0, 20*20), size=200, replace=False):
        x, y, = index // 20, index % 20
        field[y, x] = 0
    return field
