import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def signal(t):
    return 4.8 * np.sin(2 * np.pi * 25 * t)


def quantize(x, bits):
    delta = 10.0 / (2 ** bits)

    xq = np.round(x / delta) * delta
    xq = np.clip(xq, -5.0, 5.0)

    return xq, delta


def main():
    fs = 2000
    duration = 0.2

    bit_depths = [3, 4, 8, 12]

    t = np.arange(0, duration, 1 / fs)
    x = signal(t)

    quantized = {}

    print("Ошибки квантования для разных разрядностей АЦП\n")

    print(
        f"{'Биты':>8} {'Шаг Δ, В':>14} "
        f"{'Макс. ошибка, В':>20} {'СКО ошибки, В':>18}"
    )
    print("-" * 64)

    for bits in bit_depths:
        xq, delta = quantize(x, bits)

        error = x - xq

        max_error = np.max(np.abs(error))
        rmse = np.sqrt(np.mean(error ** 2))

        quantized[bits] = xq

        print(
            f"{bits:>8} {delta:>14.8f} "
            f"{max_error:>20.8f} {rmse:>18.8f}"
        )

    ts = np.linspace(0, 0.04, 1200)

    plt.figure(figsize=(11, 5))

    plt.plot(
        ts,
        signal(ts),
        label="Исходный сигнал",
        linewidth=2
    )

    for bits in [3, 8, 12]:
        plt.step(
            t,
            quantized[bits],
            where="mid",
            label=f"АЦП {bits} бит"
        )

    plt.xlim(0, 0.04)

    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.title("Влияние разрядности АЦП на форму сигнала")

    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    path = Path(__file__).with_name("zadanie_5.png")

    plt.savefig(path, dpi=150)

    print(f"\nГрафик сохранён: {path}")

    plt.show()

    print("\nВывод:")
    print("С ростом разрядности шаг квантования уменьшается.")
    print("Поэтому форма сигнала точнее приближается к исходной,")
    print("а ошибка квантования становится меньше.")


if __name__ == "__main__":
    main()