
import numpy as np
import matplotlib.pyplot as plt

x_true = 5.0
N = 10000

systems = {
    "Система A": (0.0, 0.50),
    "Система B": (0.30, 0.05),
    "Система C": (0.30, 0.50)
}

rng = np.random.default_rng(1)
results = {}

for name, (bias, sigma) in systems.items():
    measurements = x_true + bias + rng.normal(0, sigma, N)
    results[name] = measurements

print("СРАВНЕНИЕ ИЗМЕРИТЕЛЬНЫХ СИСТЕМ")
print("-" * 45)

for name, measurements in results.items():
    print(name)
    print(f"Среднее измерений: {np.mean(measurements):.4f} В")
    print(f"СКО измерений: {np.std(measurements):.4f} В")
    print()

sample_sizes = [1, 10, 100, 1000]
measurements_A = results["Система A"]
averaged_results = {}

print("ЭФФЕКТ УСРЕДНЕНИЯ ДЛЯ СИСТЕМЫ A")
print("-" * 45)

for size in sample_sizes:
    groups = measurements_A[:(N // size) * size].reshape(-1, size)
    averages = np.mean(groups, axis=1)
    averaged_results[size] = averages

    print(
        f"Усреднение по {size:4} измерениям: "
        f"СКО средних = {np.std(averages):.4f} В"
    )

plt.figure(figsize=(10, 5))

for name, measurements in results.items():
    plt.hist(
        measurements,
        bins=60,
        density=True,
        alpha=0.4,
        label=name
    )

plt.axvline(
    x_true,
    linestyle="--",
    color="black",
    label="Истинное значение: 5 В"
)
plt.title("Сравнение измерительных систем")
plt.xlabel("Измеренное напряжение, В")
plt.ylabel("Плотность")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.figure(figsize=(10, 5))

for size, averages in averaged_results.items():
    plt.hist(
        averages,
        bins=40,
        density=True,
        alpha=0.4,
        label=f"{size} измер."
    )

plt.axvline(
    x_true,
    linestyle="--",
    color="black",
    label="Истинное значение: 5 В"
)
plt.title("Эффект усреднения для системы A")
plt.xlabel("Среднее измеренное напряжение, В")
plt.ylabel("Плотность")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
