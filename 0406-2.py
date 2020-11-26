#matplotlib

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6, 601)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label = "sin")
plt.plot(x, y2, linestyle = "--", label = "cos")
plt.xlabel("x")
plt.xlabel("y")
plt.title("sin & cos")
plt.legend()
plt.show()
