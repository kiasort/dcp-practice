import numpy as np
import matplotlib.pyplot as plt

U0 = 2          
A = 1           
f0 = 10         
sigma_w = 0.25  

fs = 500        
T = 2           

N = int(fs * T)

t = np.arange(N) / fs

rng = np.random.default_rng(1)

w = rng.normal(0, sigma_w, size=len(t))



x = U0 + A * np.sin(2 * np.pi * f0 * t) + w


print("ПАРАМЕТРЫ СИГНАЛА")
print("-" * 20)
print(f"Постоянная составляющая U0 = {U0} В")
print(f"Амплитуда A = {A} В")
print(f"Частота f0 = {f0} Гц")
print(f"СКО шума sigma_w = {sigma_w} В")
print(f"Частота дискретизации fs = {fs} Гц")
print(f"Длительность записи T = {T} с")
print(f"Количество отсчётов N = {N}")



mask = t <= 0.5

plt.figure(figsize=(12, 6))

plt.plot(
    t[mask],
    x[mask],
    label='x(t) = 2 + sin(2π·10t) + w(t)'
)

plt.title('Сигнал измерительного датчика')
plt.xlabel('Время, с')
plt.ylabel('Амплитуда, В')

plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()



print()
print("ОБЪЯСНЕНИЕ")
print("-" * 20)
print("Детерминированная часть:")
print("  U0 + A*sin(2π*f0*t)")
print()
print("Случайная часть:")
print("  w(t) — гауссовский шум со средним 0")
print(f"  и СКО {sigma_w} В.")