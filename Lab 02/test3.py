import numpy as np
import matplotlib.pyplot as plt

# --- Cách 1
# Trục x và trục y
x=range(1,6)
y=[ [1,4,6,8,9], [2,2,7,10,12], [2,8,5,10,6] ]

# Biểu đồ diện tích xếp chồng cơ bản.
plt.stackplot(x,y, labels=['Đối tượng 1','Đối tượng 2','Đối tượng 3'])
plt.legend(loc='upper left')
plt.xlabel('Trục x')
plt.ylabel('Trục y')
plt.title('Cách 1_Biểu đồ diện tích xếp chồng cơ bản')
plt.show()


# --- Cách 2
x=range(1,6)
y1=[1,4,6,8,9]
y2=[2,2,7,10,12]
y3=[2,8,5,10,6]

# Biểu đồ diện tích xếp chồng cơ bản.
plt.stackplot(x,y1, y2, y3, labels=['Đối tượng 1','Đối tượng 2','Đối tượng 3'])
plt.legend(loc='upper left')
plt.xlabel('Trục x')
plt.ylabel('Trục y')
plt.title('Cách 2_Biểu đồ diện tích xếp chồng cơ bản')
plt.show()
