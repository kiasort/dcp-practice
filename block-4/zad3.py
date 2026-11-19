import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


N = 40
n = np.arange(N)
x = np.ones(N)


def calculate_output(x, feedback, input_coefficient, initial_value):
    y = np.zeros(len(x))
    previous_y = initial_value

    for i in range(len(x)):
        y[i] = feedback * previous_y + input_coefficient * x[i]
        previous_y = y[i]

    return y


y_initial_0 = calculate_output(x, 0.7, 0.3, 0)
y_initial_2 = calculate_output(x, 0.7, 0.3, 2)

y_lfilter = signal.lfilter([0.3], [1, -0.7], x)

difference = np.max(np.abs(y_initial_0 - y_lfilter))
print(f"max|y_рек - y_lfilter| = {difference:.12e}")

steady_state = 0.3 / (1 - 0.7)
print(f"Стационарный предел: y_inf = {steady_state:.6f}")
print(f"Последнее значение при y[-1] = 0: {y_initial_0[-1]:.6f}")
print(f"Последнее значение при y[-1] = 2: {y_initial_2[-1]:.6f}")

plt.figure(figsize=(10, 5))
plt.stem(n, y_initial_0, label="Начальное условие y[-1] = 0")
plt.stem(n, y_initial_2, label="Начальное условие y[-1] = 2")
plt.title("Переходные характеристики при разных начальных условиях")
plt.xlabel("Номер отсчёта n")
plt.ylabel("Выход y[n]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

unstable_feedback = 1.05
y_unstable = calculate_output(x, unstable_feedback, 0.3, 0)

print("\nСистема с коэффициентом обратной связи 1.05:")
print(f"Последнее значение: {y_unstable[-1]:.6f}")
print(f"Максимальное значение: {np.max(np.abs(y_unstable)):.6f}")

plt.figure(figsize=(10, 5))
plt.stem(n, y_unstable)
plt.title("Выход системы при коэффициенте обратной связи 1.05")
plt.xlabel("Номер отсчёта n")
plt.ylabel("Выход y[n]")
plt.grid(True)
plt.tight_layout()
plt.show()