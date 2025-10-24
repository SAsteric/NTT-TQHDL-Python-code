import matplotlib.pyplot as plt
import numpy as np

#line 1
x_point = np.array([20,22,24,26,28,30])
y_point = np.array([5,4,6,4,6,8])
plt.plot(x_point, y_point, color = 'r', label='Nhớt')

#line 2
y_point2 = np.array([4,4.5,5,3,4,7])
plt.plot(x_point, y_point2, color = 'g', label='Dầu')

#line 3
y_point3 = np.array([5,3,5,4,5,5])
plt.plot(x_point, y_point3, color = 'b', label='Xăng')

#Labels
plt.xlabel('Giá nhiên liệu (VND)')
plt.ylabel('Thời gian (Tháng)')
plt.title('Biểu đồ nhiên liệu trong nước (năm 2020)')

plt.legend() #Không hiểu sao mà phải có cái này mới xuất ra label của lines :)
plt.show()