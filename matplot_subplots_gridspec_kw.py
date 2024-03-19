import matplotlib.pyplot as plt
import numpy as np

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html
# https://qiita.com/MtNouchi/items/7818ed83e825938cdcae
# https://pystyle.info/matplotlib-sharex-sharey/
# https://qiita.com/nkay/items/d1eb91e33b9d6469ef51

fig, axes = plt.subplots(
    2, # 縦
    1, # 横
    gridspec_kw=dict(width_ratios=[1], height_ratios=[4, 1], wspace=0.1, hspace=0.3),
    sharex='col',
    sharey='row',
    figsize=(12, 8)
)
fig.suptitle("title")

for i, ax in enumerate(axes):
    j = i + 1
    x = np.arange(100)
    y = np.arange(100, 200) * j

    ax.grid()
    ax.plot(x, y)
    ax.set_title(f"title {j}")
    ax.set_xlabel(f"x axis {j}")
    ax.set_ylabel(f"y axis {j}")

plt.show()
