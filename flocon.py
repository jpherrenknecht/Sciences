from fractal import koch
import numpy as np
import matplotlib.pylab as plt

a = np.array([[0], [0]])
b = np.array([[1], [0]])
c = np.array([[.5], [np.sqrt(3)/2]])


koch(b, a, 5, np.pi / 3.)
koch(a, c, 5, np.pi / 3.)
koch(c, b, 5, np.pi / 3.)

plt.axis('off')
plt.show()
