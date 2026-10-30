import numpy as np
import matplotlib.pyplot as plt


U0 = 0.0          
A = 1.0           
f0 = 2.0          
phi = 0.0         
sigma_w = 0.0     

T = 1 / f0        
duration = 2 * T  
N = 1000          

t = np.linspace(0, duration, N)



noise = np.random.normal(0, sigma_w, N)

x = U0 + A * np.sin(2 * np.pi * f0 * t + phi) + noise


mu = np.mean(x)


D = np.var(x)


sigma = np.std(x)


RMS = np.sqrt(np.mean(x ** 2))

mu_theory = U0
D_theory = A**2 / 2
sigma_theory = A / np.sqrt(2)
RMS_theory = np.sqrt(U0**2 + A**2 / 2)


print("=" * 60)
print("ЗАДАНИЕ 2 — РАСЧЁТ ПАРАМЕТРОВ СИГНАЛА")
print("ВАРИАНТ 1")
print("=" * 60)

print("\nПАРАМЕТРЫ СИГНАЛА:")
print("-" * 60)
print(f"U0              = {U0:.2f} В")
print(f"A               = {A:.2f} В")
print(f"f0              = {f0:.2f} Гц")
print(f"phi             = {phi:.2f} рад")
print(f"СКО шума        = {sigma_w:.2f} В")

print("\nМОДЕЛЬ СИГНАЛА:")
print("-" * 60)
print("x(t) = sin(2π · 2t)")

print("\nРАСЧЁТНЫЕ ЗНАЧЕНИЯ:")
print("-" * 60)
print(f"Среднее значение μ    = {mu:.4f} В")
print(f"Дисперсия D           = {D:.4f} В²")
print(f"СКО σ                 = {sigma:.4f} В")
print(f"СКЗ                   = {RMS:.4f} В")

print("\nТЕОРЕТИЧЕСКИЕ ЗНАЧЕНИЯ:")
print("-" * 60)
print(f"Среднее значение μ    = {mu_theory:.4f} В")
print(f"Дисперсия D           = {D_theory:.4f} В²")
print(f"СКО σ                 = {sigma_theory:.4f} В")
print(f"СКЗ                   = {RMS_theory:.4f} В")

print("\nОТКЛОНЕНИЕ ОТ ТЕОРЕТИЧЕСКИХ ЗНАЧЕНИЙ:")
print("-" * 60)
print(f"μ:   {abs(mu - mu_theory):.6f} В")
print(f"D:   {abs(D - D_theory):.6f} В²")
print(f"σ:   {abs(sigma - sigma_theory):.6f} В")
print(f"СКЗ: {abs(RMS - RMS_theory):.6f} В")


print("Сигнал представляет собой чистую синусоиду")
print("без постоянной составляющей и шума.")
print("Среднее значение близко к нулю.")
print("СКЗ и СКО практически совпадают.")




plt.figure(figsize=(10, 5))

plt.plot(t, x, label="x(t) = sin(2π·2t)")

plt.axhline(
    mu,
    linestyle="--",
    label=f"Среднее μ = {mu:.4f} В"
)

plt.axhline(
    0,
    linestyle=":",
    label="Нулевая линия"
)

plt.title("Сигнал — вариант 1")
plt.xlabel("Время, с")
plt.ylabel("Амплитуда, В")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()