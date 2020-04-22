import matplotlib.pyplot as plt
import numpy as np


labels = ['Hexahedral Mesh', 'Hexahedral Mesh']
men_means = [341.6, 394.6]
women_means = [407, 639]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width,label='Times')
ax2 = ax.twinx()
rects2 = ax2.bar(x + width/2, women_means, width, color = 'c', label='RunTimes')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax2.legend()

fig.tight_layout()

plt.show()