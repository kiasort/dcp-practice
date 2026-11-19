import numpy as np
import matplotlib.pyplot as plt

N = 25
n = np.arange(N)

u0 = np.ones(N)
u1 = np.zeros(N)
u1[0] = 1

h = np.zeros(N)
h[:3] = [1, 0, 0]

g = np.convolve(u0, h)[:N]

print("Переходная характеристика:")
print(f"g[0] = {g[0]}")
print(f"g[1] = {g[1]}")
print(f"g[2] = {g[2]}")
print(f"g[3] = {g[3]}")

fig, axes = plt.subplots(4, 1, figsize=(10, 9))

axes[0].stem(n, u0)
axes[0].set_title("Единичный скачок u0[n]")
axes[0].set_xlabel("Номер отсчёта n")
axes[0].set_ylabel("Амплитуда")
axes[0].grid(True)

axes[1].stem(n, h)
axes[1].set_title("Импульсная характеристика h[n]")
axes[1].set_xlabel("Номер отсчёта n")
axes[1].set_ylabel("Амплитуда")
axes[1].grid(True)

axes[2].stem(n, u1)
axes[2].set_title("Единичный импульс u1[n]")
axes[2].set_xlabel("Номер отсчёта n")
axes[2].set_ylabel("Амплитуда")
axes[2].grid(True)

axes[3].stem(n, g)
axes[3].set_title("Переходная характеристика g[n]")
axes[3].set_xlabel("Номер отсчёта n")
axes[3].set_ylabel("Амплитуда")
axes[3].grid(True)

plt.tight_layout()
plt.show()