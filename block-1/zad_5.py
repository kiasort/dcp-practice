
import numpy as np
import matplotlib.pyplot as plt

f0 = 5
frequencies = [100, 40, 15, 8]
duration = 1

print("ЗАДАНИЕ 5")
print("-" * 65)
print(f"{'f0, Гц':<12}{'fs, Гц':<12}{'Отсчётов за период':<22}Наблюдение")

for fs in frequencies:
    samples_per_period = fs / f0

    if fs > 2 * f0:
        if samples_per_period >= 8:
            observation = "Хорошее представление"
        else:
            observation = "Мало отсчётов"
    else:
        observation = "Нарушение Найквиста"

    print(f"{f0:<12}{fs:<12}{samples_per_period:<22.2f}{observation}")

fig, axes = plt.subplots(4, 1, figsize=(10, 12))

for ax, fs in zip(axes, frequencies):
    t = np.arange(0, duration, 1 / fs)
    x = np.sin(2 * np.pi * f0 * t)

    t_continuous = np.linspace(0, duration, 2000)
    x_continuous = np.sin(2 * np.pi * f0 * t_continuous)

    ax.plot(t_continuous, x_continuous, alpha=0.6, label="Исходный сигнал")
    ax.stem(t, x, linefmt="C1-", markerfmt="C1o", basefmt="k-", label="Отсчёты")
    ax.set_title(f"f0 = {f0} Гц, fs = {fs} Гц")
    ax.set_xlabel("Время, с")
    ax.set_ylabel("Амплитуда")
    ax.grid(True)
    ax.legend()

plt.tight_layout()
plt.show()
