import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

fig, ax = plt.subplots(figsize=(8, 4))

x    = np.arange(100)
y    = np.arange(100,200)
sample_df = pd.DataFrame( {'x' : x, 'y' : y })


ax.plot(sample_df["x"], sample_df["y"])
plt.text(0, 150, "0-10", rotation='vertical')

ax.axvspan(10, 20, color="gray", alpha=0.3, label="10-20")
plt.text(10, 150, "10-20", rotation='vertical')

ax.axvspan(30, 40, color="gray", alpha=0.3)
plt.text(30, 150, "30-40", rotation='vertical')

ax.axvspan(50, 60, color="gray", alpha=0.3)
plt.text(50, 150, "50-60", rotation='vertical')

ax.axvspan(70, 80, color="gray", alpha=0.3)
plt.text(70, 150, "70-80", rotation='vertical')

ax.grid()
labels = ax.get_xticklabels()
plt.setp(labels, rotation=90, fontsize=12);
ax.set_title("test")
plt.show()
