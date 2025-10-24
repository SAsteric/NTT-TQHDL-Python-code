import matplotlib.pyplot as plt
import numpy as np

#line 1
x_point = np.array([1,3,6,9,15])
y_point = np.array([10,9,25,15, 50])
plt.plot(x_point, y_point, linestyle = ':', color = 'g')

#line 2
x_point2 = np.array([1,3,7,13])
y_point2 = np.array([9,24,15, 45])
plt.plot(x_point2, y_point2, linestyle = 'dashed', color = 'r')


plt.show()