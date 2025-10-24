import numpy as np
import matplotlib.pyplot as plt


fig, axes = plt.subplots(1, 3, figsize=(10, 4), sharey=True, dpi=120)

fig.patch.set_facecolor("white")


plots = [
    {"x": [0, 1, 4, 6, 5], "y": [1, 2, 3, 5, 6], "color": "g", "label": "green color"},
    {"x": [0, 1, 2, 7], "y": [10, 4, 3, 2], "color": "r", "label": "red color"},
    {"x": [0.5, 1.5, 2.5, 2.5, 2.5], "y": [10, 7, 5, 3, 1], "color": "b", "label": "blue color"},
]


for ax, p in zip(axes, plots):
    ax.plot(p["x"], p["y"], color=p["color"], marker='o', label=p["label"])
    ax.set_title(p["label"])
    ax.set_facecolor('#e5e5e5')  # gray only inside subplot
    ax.grid(True, color='white', linewidth=1.2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 12)

plt.tight_layout()
plt.show()
