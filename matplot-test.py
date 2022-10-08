import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

fig, ax = plt.subplots(figsize=(8, 4))

x    = np.arange(100)
y    = np.arange(100,200)
sample_df = pd.DataFrame( {'x' : x, 'y' : y })


ax.plot(sample_df["x"], sample_df["y"])
ax.axvspan(10, 20, color="gray", alpha=0.3)
ax.axvspan(30, 40, color="gray", alpha=0.3)
ax.axvspan(50, 60, color="gray", alpha=0.3)
ax.axvspan(70, 80, color="gray", alpha=0.3)
ax.grid()
labels = ax.get_xticklabels()
plt.setp(labels, rotation=90, fontsize=12);
ax.set_title("test")
plt.show()
