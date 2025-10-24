import matplotlib.pyplot as plt


x_green = [0,1,2,3,4]
y_green = [1,2,3,4,10]

x_red = [0,1,2,3,4]
y_red = [10,4,3,2,1]

x_blue = [2.5,2.5,2.5,1.5,0.5]
y_blue = [1,3,5,7,10]

x_yellow = [0,1.4,2,5,6]
y_yellow = [3,2,3,5,8]

#draw lines
plt.plot(x_green, y_green, color='g', marker='o', label='green color')
plt.plot(x_red, y_red, color='r', marker='o', label='red color')
plt.plot(x_blue, y_blue, color='b', marker='o', label='blue color')
plt.plot(x_yellow, y_yellow, color='y', marker='o', label='yellow color')

#title
plt.title('Line in Python Matplotlib')

#background color
bg = plt.gca()
bg.set_facecolor("#e5e5e5")

plt.legend()
plt.grid(True)
plt.show()