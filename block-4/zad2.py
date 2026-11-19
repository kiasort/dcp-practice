import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

N = 40
d = 2
c = 1

n = np.arange(N)

h = np.zeros(N)
h[0] = 1

x = np.zeros(N)
x[0] = 1
x[d] = c

h_shifted = np.zeros(N)
h_shifted[d:] = h[:-d]

y_manual = h + c * h_shifted

y_conv = np.convolve(x, h)[:N]
y_lfilter = signal.lfilter(h, [1], x)

print("Максимальные отклонения:")
print(f"max|y_ручн - y_conv| = {np.max(np.abs(y_manual - y_conv)):.12e}")
print(f"max|y_conv - y_lfilter| = {np.max(np.abs(y_conv - y_lfilter)):.12e}")

fig, axes = plt.subplots(5, 1, figsize=(10, 12))

signals = [
    (x, "Входной сигнал x[n]"),
    (h, "Импульсная характеристика h[n]"),
    (y_manual, "Выход, вычисленный вручную"),
    (y_conv, "Выход через свёртку np.convolve"),
    (y_lfilter, "Выход через signal.lfilter")
]

for ax, (values, title) in zip(axes, signals):
    ax.stem(n, values)
    ax.set_title(title)
    ax.set_xlabel("Номер отсчёта n")
    ax.set_ylabel("Амплитуда")
    ax.grid(True)

plt.tight_layout()
plt.show()