import matplotlib.pyplot as plt
import numpy as np
import psutil

num = 1000
mem_ary = np.empty(0)

for i in range(num):
    # メモリサイズが大きいグラフを描画
    x = np.arange(1e7)
    y = np.arange(1e7)
    fig, ax = plt.subplots()
    ax.plot(x, y)

    ## パターン2
    #plt.clf()
    #plt.close()

    fig.clear()
    plt.close(fig)

    # ===================================================

    # メモリ使用量を記録
    mem = psutil.virtual_memory().used / 1e9
    mem = round(mem, 1)
    mem_ary = np.append(mem_ary, mem)
    print(f"{i}: {mem}")

x = np.arange(num)
print(mem_ary)
plt.plot(x, mem_ary)
print("showing...")
plt.show()
print("showed")
