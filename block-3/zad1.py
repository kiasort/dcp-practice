import numpy as np
import matplotlib.pyplot as plt

fs = 1000
n = np.arange(1000)
t = n / fs

x1 = np.sin(2 * np.pi * 5 * t)
x2 = 0.5 * np.sin(2 * np.pi * 15 * t)
x = x1 + x2

def system(signal):
    delayed = np.zeros_like(signal)
    delayed[20:] = signal[:-20]
    return 0.5 * signal + 0.5 * delayed

y = system(x)
y1 = system(x1)
y2 = system(x2)

difference = y - (y1 + y2)

print("Проверка принципа суперпозиции")
print(f"Максимальное отклонение: {np.max(np.abs(difference)):.12e}")

print("\nАмплитудные характеристики")
gain_5 = abs(np.cos(10 * 2 * np.pi * 5 / fs))
gain_15 = abs(np.cos(10 * 2 * np.pi * 15 / fs))

print(f"Коэффициент передачи для 5 Гц: {gain_5:.4f}")
print(f"Коэффициент передачи для 15 Гц: {gain_15:.4f}")

print("\nЗадержка системы:")
print(f"10 отсчетов = {10 / fs:.3f} с")

fig, axes = plt.subplots(3, 1, figsize=(12, 9))

axes[0].plot(t, x1, label="Сигнал 5 Гц")
axes[0].plot(t, x2, label="Сигнал 15 Гц")
axes[0].plot(t, x, label="Суммарный сигнал")
axes[0].set_title("Входные сигналы")
axes[0].set_xlabel("Время, с")
axes[0].set_ylabel("Амплитуда")
axes[0].legend()
axes[0].grid()

axes[1].plot(t, x, label="Входной сигнал")
axes[1].plot(t, y, label="Выходной сигнал")
axes[1].set_title("Входной и выходной сигналы")
axes[1].set_xlabel("Время, с")
axes[1].set_ylabel("Амплитуда")
axes[1].set_xlim(0, 0.2)
axes[1].legend()
axes[1].grid()

axes[2].plot(t, y1, label="Выход от сигнала 5 Гц")
axes[2].plot(t, y2, label="Выход от сигнала 15 Гц")
axes[2].set_title("Выходные составляющие")
axes[2].set_xlabel("Время, с")
axes[2].set_ylabel("Амплитуда")
axes[2].set_xlim(0, 0.2)
axes[2].legend()
axes[2].grid()

plt.tight_layout()
plt.show()