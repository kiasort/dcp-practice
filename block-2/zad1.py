import numpy as np


def main():
    types = [
        ("uint8", np.uint8),
        ("int8", np.int8),
        ("uint16", np.uint16),
        ("int16", np.int16),
        ("float32", np.float32),
        ("float64", np.float64)
    ]

    print("Диапазоны значений числовых типов NumPy\n")

    print(
        f"{'Тип':<10} {'Биты':>6} {'Минимум':>24} "
        f"{'Максимум':>24} {'Число целых значений':>24}"
    )
    print("-" * 94)

    for name, dtype in types:
        bits = np.dtype(dtype).itemsize * 8

        if np.issubdtype(dtype, np.integer):
            info = np.iinfo(dtype)
            count = int(info.max) - int(info.min) + 1

            print(
                f"{name:<10} {bits:>6} {int(info.min):>24} "
                f"{int(info.max):>24} {count:>24}"
            )
        else:
            info = np.finfo(dtype)

            print(
                f"{name:<10} {bits:>6} {info.min:>24.6e} "
                f"{info.max:>24.6e} {'—':>24}"
            )

    print("\nВывод:")
    print("Целочисленные типы имеют конечный диапазон значений.")
    print("Беззнаковые типы не хранят отрицательные числа.")
    print("Вещественные типы поддерживают дробные значения,")
    print("но имеют ограниченную точность.")


if __name__ == "__main__":
    main()