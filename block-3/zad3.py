import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

fs = 2000
T0 = 0.2
f0 = 5
N = 5

dt = 1 / fs
t = np.arange(0, T0, dt)

def signal(t):
    return 1 + 2 * np.cos(2 * np.pi * 5 * t) - 0.5 * np.sin(2 * np.pi * 10 * t)

x = signal(t)

t_integral = np.linspace(0, T0, len(t) + 1)
x_integral = signal(t_integral)

a0 = (2 / T0) * trapezoid(x_integral, t_integral)

an = []
bn = []

for k in range(1, N + 1):
    a = (2 / T0) * trapezoid(
        x_integral * np.cos(2 * np.pi * k * f0 * t_integral),
        t_integral
    )

    b = (2 / T0) * trapezoid(
        x_integral * np.sin(2 * np.pi * k * f0 * t_integral),
        t_integral
    )

    an.append(a)
    bn.append(b)

print("Коэффициенты ряда Фурье:")
print(f"a0 = {a0:.6f}")

print("\n n       an          bn")
for k in range(N):
    print(f"{k + 1}   {an[k]:10.6f}   {bn[k]:10.6f}")

x_reconstructed = np.full_like(t, a0 / 2)

for k in range(1, N + 1):
    x_reconstructed += (
        an[k - 1] * np.cos(2 * np.pi * k * f0 * t)
        + bn[k - 1] * np.sin(2 * np.pi * k * f0 * t)
    )

plt.figure(figsize=(10, 5))
plt.plot(t, x, label="Исходный сигнал")
plt.title("Исходный сигнал за один период")
plt.xlabel("Время, с")
plt.ylabel("Амплитуда")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(t, x, label="Исходный сигнал")
plt.plot(t, x_reconstructed, "--", label="Восстановленный сигнал")
plt.title("Восстановление сигнала с помощью ряда Фурье")
plt.xlabel("Время, с")
plt.ylabel("Амплитуда")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()