import pandas as pd
import matplotlib.pyplot as plt



df = pd.DataFrame({
'x': range(1,7),
'y1': [15,4,8,6,3,5],
'y2': [10,2,7,12,1,9],
'y3': [7,15,5,8,2,14]
})

plt.figure(figsize=(10,6))


plt.stackplot(df['x'], df['y1'], df['y2'], df['y3'], 
            colors=['red', 'orange', 'blue'],
            alpha=0.8)

plt.xlabel('Trục x', fontsize=12)
plt.ylabel('Trục y', fontsize=12)
plt.title('Biểu đồ stackplot', fontsize=14)
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.xticks(df['x'])

plt.tight_layout()
plt.show()