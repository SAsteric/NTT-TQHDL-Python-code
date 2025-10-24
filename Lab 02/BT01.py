import numpy as np
import matplotlib.pyplot as plt


x_point = np.linspace(-20,20,80)
y_point = np.sin(x_point)

#draw line
plt.plot(x_point, y_point, 'r--', linewidth=4)

#cho background co mau
bg = plt.gca()
bg.set_facecolor("#e5e5e5")

#labels
plt.xlabel('X Value')
plt.ylabel('Sin of X')
plt.title('Hàm Sin')


plt.show()
