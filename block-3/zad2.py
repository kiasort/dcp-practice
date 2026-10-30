import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

t = sp.symbols('t', real=True, positive=True)
s = sp.symbols('s')

a = 2
omega = 2 * sp.pi * 5

x = sp.exp(-a * t) * sp.sin(omega * t)

X = sp.laplace_transform(x, t, s, noconds=True)
X = sp.simplify(X)

print("Преобразование Лапласа:")
print("X(s) =", X)

poles = sp.solve((s + a)**2 + omega**2, s)

print("\nПолюса:")
for pole in poles:
    print(sp.simplify(pole))

print("\nЧисленные значения полюсов:")
for pole in poles:
    print(complex(pole.evalf()))

t_values = np.linspace(0, 2, 1000)
x_values = np.exp(-2 * t_values) * np.sin(10 * np.pi * t_values)

plt.figure(figsize=(10, 5))
plt.plot(t_values, x_values, label="x(t)")
plt.title("Исходный сигнал")
plt.xlabel("Время, с")
plt.ylabel("Амплитуда")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

poles_numeric = [complex(pole.evalf()) for pole in poles]

plt.figure(figsize=(7, 7))

for pole in poles_numeric:
    plt.scatter(pole.real, pole.imag, marker="x", s=100, label="Полюс")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.title("Расположение полюсов на комплексной плоскости")
plt.xlabel("Действительная часть")
plt.ylabel("Мнимая часть")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()