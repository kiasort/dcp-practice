
import numpy as np
import matplotlib.pyplot as plt

N = 10000
mu = 0
sigma_w = 0.25

rng = np.random.default_rng(1)
w = rng.normal(mu, sigma_w, N)

counts, bins, patches = plt.hist(
    w,
    bins=50,
    density=True,
    alpha=0.7,
    edgecolor="black"
)

bin_widths = np.diff(bins)
area = np.sum(counts * bin_widths)

plt.title("Гистограмма случайного шума")
plt.xlabel("Значение шума, В")
plt.ylabel("Плотность")
plt.grid(True)
plt.tight_layout()
plt.show()

print("ЗАДАНИЕ 3")
print(f"Среднее значение шума: {np.mean(w):.4f} В")
print(f"СКО шума: {np.std(w):.4f} В")
print(f"Площадь под гистограммой: {area:.4f}")
print(f"Проверка нормировки: {'выполнена' if np.isclose(area, 1) else 'не выполнена'}")
