import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def signal(t):
    return 4.8 * np.sin(2 * np.pi * 25 * t)


def main():
    fs = 2000
    duration = 0.2
    bits = 12

    adc_min = -5.0
    adc_max = 5.0

    levels = 2 ** bits
    delta = (adc_max - adc_min) / levels

    t = np.arange(0, duration, 1 / fs)
    x = signal(t)

    xq = np.round(x / delta) * delta
    xq = np.clip(xq, adc_min, adc_max)

    t_smooth = np.linspace(0, duration, 4000)
    x_smooth = signal(t_smooth)

    print("Моделирование 12-битного АЦП\n")

    print(f"Число уровней L = 2^{bits} = {levels}")
    print(
        f"Шаг квантования Δ = "
        f"({adc_max} - ({adc_min})) / {levels} = {delta:.9f} В"
    )
    print(f"Количество отсчётов: {len(t)}")

    print(f"Минимум сигнала: {x.min():.6f} В")
    print(f"Максимум сигнала: {x.max():.6f} В")

    plt.figure(figsize=(11, 5))

    plt.plot(
        t_smooth,
        x_smooth,
        label="Исходный сигнал",
        linewidth=1.8
    )

    plt.step(
        t,
        xq,
        where="mid",
        label="Квантованный сигнал (12 бит)"
    )

    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.title("Моделирование 12-битного АЦП")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    path = Path(__file__).with_name("zadanie_4.png")

    plt.savefig(path, dpi=150)

    print(f"\nГрафик сохранён: {path}")

    plt.show()

    print("\nВывод:")
    print("12-битный АЦП имеет 4096 кодовых уровней.")
    print("Квантование заменяет значения сигнала ближайшими")
    print("дискретными уровнями.")


if __name__ == "__main__":
    main()