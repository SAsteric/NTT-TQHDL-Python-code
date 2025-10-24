import numpy as np
import matplotlib.pyplot as plt


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (10,4), sharey=True, dpi = 120)

x_green = [0,1,4,6,5]
y_green = [1,2,3,5,6]

x_red = [0,1,2,7]
y_red = [10,4,3,2]

x_blue = [0.5,1.5,2.5,2.5,2.5]
y_blue = [10,7,5,3,1]


ax1.plot(x_green, y_green, color='g', marker='o', label='green color')
ax1.set_title('green color')
ax1.set_facecolor('#e5e5e5')
ax1.grid(True, color='white', linewidth=1.2)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_xlim(0, 6)
ax1.set_ylim(0, 12)

ax2.plot(x_red, y_red, color='r', marker='o', label='red color')
ax2.set_title('red color')
ax2.set_facecolor('#e5e5e5')
ax2.grid(True, color='white', linewidth=1.2)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_xlim(0, 6)
ax2.set_ylim(0, 12)

ax3.plot(x_blue, y_blue, color='b', marker='o', label='blue color')
ax3.set_title('blue color')
ax3.set_facecolor('#e5e5e5')
ax3.grid(True, color='white', linewidth=1.2)
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_xlim(0, 6)
ax3.set_ylim(0, 12)


#background color
bg = plt.gca()
bg.set_facecolor("#e5e5e5")


plt.tight_layout()
plt.show()