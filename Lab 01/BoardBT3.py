import matplotlib.pyplot as plt
import numpy as np

x_point = np.array([1,2,3,5,7])
y_point = np.array([5.0,1.5,5.0,20.0,10.0])

plt.plot(x_point, y_point, 'bD--', color = 'r')

plt.show()