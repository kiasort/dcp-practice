
import numpy as np
import matplotlib.pyplot as plt

A = 1
f0 = 5
fs = 100
duration = 1

t = np.arange(0, duration, 1 / fs)
x = A * np.sin(2 * np.pi * f0 * t)

def quantize(signal, levels):
    step = 2 * A / (levels - 1)
    quantized = np.round((signal + A) / step) * step - A
    return np.clip(quantized, -A, A)

x4 = quantize(x, 4)
x8 = quantize(x, 8)
x16 = quantize(x, 16)

print("ЗАДАНИЕ 6")
print("-" * 45)

for name, signal in [("4 уровня", x4), ("8 уровней", x8), ("16 уровней", x16)]:
    print(f"{name}: реально использовано уровней = {len(np.unique(signal))}")

plt.figure(figsize=(12, 6))

plt.plot(t, x, "o-", markersize=2, label="Дискретный сигнал")
plt.step(t, x4, where="mid", label="Цифровой сигнал: 4 уровня")
plt.step(t, x16, where="mid", label="Цифровой сигнал: 16 уровней")

plt.title("Сравнение дискретного и квантованных сигналов")
plt.xlabel("Время, с")
plt.ylabel("Амплитуда")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.step(t, x4, where="mid", label="4 уровня")
plt.step(t, x8, where="mid", label="8 уровней")
plt.step(t, x16, where="mid", label="16 уровней")

plt.title("Сравнение квантования по амплитуде")
plt.xlabel("Время, с")
plt.ylabel("Амплитуда")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
