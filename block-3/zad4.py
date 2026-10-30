import numpy as np
import matplotlib.pyplot as plt

n = np.arange(30)

coefficients = [0.8, 1.05]

for a in coefficients:
    x = a ** n

    print(f"\nКоэффициент a = {a}")
    print(f"X(z) = 1 / (1 - {a}z^(-1))")
    print(f"Полюс: z = {a}")
    print(f"Область сходимости: |z| > {a}")

    if abs(a) < 1:
        print("Система устойчива")
    else:
        print("Система неустойчива")

    plt.figure(figsize=(10, 5))
    plt.stem(n, x)
    plt.title(f"Последовательность x[n] = {a}^n")
    plt.xlabel("Номер отсчета n")
    plt.ylabel("Амплитуда")
    plt.grid()
    plt.tight_layout()
    plt.show()

    theta = np.linspace(0, 2 * np.pi, 500)

    unit_circle_x = np.cos(theta)
    unit_circle_y = np.sin(theta)

    plt.figure(figsize=(7, 7))
    plt.plot(unit_circle_x, unit_circle_y, label="Единичная окружность")
    plt.scatter(a, 0, marker="x", s=100, label="Полюс")

    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)

    plt.title(f"Полюс на комплексной плоскости, a = {a}")
    plt.xlabel("Действительная часть")
    plt.ylabel("Мнимая часть")
    plt.axis("equal")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()