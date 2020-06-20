import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 255, 1)
y = -255 / 2 * np.cos(4 * np.pi * x / 255) + 255/2

plt.plot(x, y)

plt.savefig("tone.png")