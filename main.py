import seedPatterns
from field import Field

import numpy as np
import matplotlib.pyplot as plt

# Write your code here
# Simulate the growth for a season of 100 days with a random field at 90% capacity
# Can you display a heatmap of the average height over multiple seasons ?
# What pattern emerges and how is it related to the growth factors?

field = Field(seedPattern=seedPatterns.random90())
