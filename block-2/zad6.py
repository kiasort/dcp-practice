import numpy as np


def accumulate(dtype, checkpoints):
    total = dtype(0.0)
    results = {}

    for i in range(1, max(checkpoints) + 1):
        total = dtype(total + dtype(0.1))

        if i in checkpoints:
            results[i] = float(total)

    return results


def main():
    checkpoints = [
        1_000,
        10_000,
        100_000,
        1_000_000
    ]

    sums32 = accumulate(np.float32, checkpoints)
    sums64 = accumulate(np.float64, checkpoints)

    print("Накопление ошибки округления при сложении 0.1\n")

    print(
        f"{'N':>10} "
        f"{'Ожидаемое':>14} "
        f"{'Сумма float32':>18} "
        f"{'Ошибка float32':>18} "
        f"{'Сумма float64':>22} "
        f"{'Ошибка float64':>18}"
    )

    print("-" * 106)

    for n in checkpoints:
        expected = n * 0.1

        s32 = sums32[n]
        s64 = sums64[n]

        error32 = s32 - expected
        error64 = s64 - expected

        print(
            f"{n:>10} "
            f"{expected:>14.6f} "
            f"{s32:>18.9f} "
            f"{error32:>18.9f} "
            f"{s64:>22.12f} "
            f"{error64:>18.10e}"
        )

    print("\nВывод:")
    print("float32 имеет меньшую точность, поэтому округление")
    print("на каждом шаге заметнее и ошибки накапливаются.")
    print("float64 хранит больше значащих цифр, поэтому")
    print("итоговая ошибка существенно меньше.")


if __name__ == "__main__":
    main()