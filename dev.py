#!/opt/homebrew/bin/python3
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import mplcursors

fig, ax = plt.subplots()
fig.set_size_inches(8, 4)
fig.canvas.manager.set_window_title('简单折线图')
ax.plot([0, 1, 2, 3, 4], [1, 4, 2, 3, 9]);
ax.legend()
mplcursors.cursor(hover = True)
plt.show()
