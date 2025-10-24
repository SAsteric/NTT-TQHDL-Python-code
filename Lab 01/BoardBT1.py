import matplotlib.pyplot as plt
import numpy as np

x_point = np.array([1,3,6,9,15])
y_point = np.array([10,9,25,15, 50])
plt.plot(x_point, y_point, linestyle = ':', color = 'g')

plt.show()