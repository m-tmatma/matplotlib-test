'''
sample code for axvspan and axhspan
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots(figsize=(8, 4))

x    = np.arange(100)
y    = np.arange(100,200)
sample_df = pd.DataFrame( {'x' : x, 'y' : y })
ax.plot(sample_df["x"], sample_df["y"])
ax.text(0, 150, "0-10", rotation='vertical')

# x = 10 ～ 20 の範囲を塗りつぶす
ax.axvspan(10, 20, color="gray", alpha=0.2, label="10-20")

# (10, 150) の位置に縦方向に "10-20" というテキストを表示する
ax.text(10, 150, "10-20", rotation='vertical')

# x = 30 ～ 40 の範囲を塗りつぶす
ax.axvspan(30, 40, color="gray", alpha=0.3)

# (30, 150) の位置に縦方向に "30-40" というテキストを表示する
ax.text(30, 150, "30-40", rotation='vertical')

# x = 50 ～ 60 の範囲を塗りつぶす
ax.axvspan(50, 60, color="gray", alpha=0.4)

# (50, 150) の位置に縦方向に "50-60" というテキストを表示する
ax.text(50, 150, "50-60", rotation='vertical')

# x = 70 ～ 80 の範囲を塗りつぶす
ax.axvspan(70, 80, color="gray", alpha=0.5)

# (70, 150) の位置に縦方向に "70-80" というテキストを表示する
ax.text(70, 150, "70-80", rotation='vertical')

# x = 90 ～ 100 の範囲を塗りつぶす
ax.axvspan(90, 100, color="gray", alpha=0.1)
ax.text(90, 150, "90-", rotation='vertical')

# y = 120 ～ 130 の範囲を塗りつぶす
ax.axhspan(120, 130, color="green", alpha=0.7, label="120-130")

# (0, 125) の位置に縦方向に "120-130" というテキストを表示する
ax.text(0, 125, "120-130")

ax.grid()
labels = ax.get_xticklabels()

# rotation=90 で x 軸の目盛りを回転して表示する
plt.setp(labels, rotation=90, fontsize=12)
ax.set_title("test")
plt.show()
