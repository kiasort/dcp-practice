import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 2, 1/fs)

A, f, phi = 1.0, 5, np.pi/4
s1 = A*np.sin(2*np.pi*f*t + phi)

A1, f1 = 1.0, 5
A2, f2 = 0.7, 20
s2 = A1*np.sin(2*np.pi*f1*t) + A2*np.sin(2*np.pi*f2*t)

s3 = np.zeros_like(t)
s3[(t >= 0.5) & (t <= 1.0)] = 1.0

np.random.seed(0)
s4 = np.random.randn(t.size)

fig, ax = plt.subplots(5, 1, figsize=(10, 12))

ax[0].plot(t, s1)
ax[0].set_title('Гармонический сигнал')
ax[1].plot(t, s2)
ax[1].set_title('Сумма двух синусоид')
ax[2].plot(t, s3)
ax[2].set_title('Одиночный импульс')
ax[3].plot(t, s4)
ax[3].set_title('Случайный сигнал')
ax[3].set_xlabel('t, с')

for a in ax[:4]:
    a.grid(True)
    a.set_ylabel('s(t)')

columns = ['Сигнал', 'Детерминированный или случайный', 'Периодический или непериодический', 'Аргумент']
rows = [
    ['Синусоида', 'Детерминированный', 'Периодический, T = 1/f', 't'],
    ['Сумма двух синусоид', 'Детерминированный', 'Периодический, если f1/f2 рационально', 't'],
    ['Одиночный импульс', 'Детерминированный', 'Непериодический', 't'],
    ['Случайный сигнал', 'Случайный', 'Непериодический', 't'],
]

ax[4].axis('off')
table = ax[4].table(cellText=rows, colLabels=columns, cellLoc='center', loc='upper center')
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1, 1.8)

widths = [0.18, 0.24, 0.38, 0.12]
for i, w in enumerate(widths):
    for j in range(len(rows) + 1):
        table[(j, i)].set_width(w)

print(f"{columns[0]:<22}{columns[1]:<32}{columns[2]:<52}{columns[3]}")
print('-' * 120)
for r in rows:
    print(f"{r[0]:<22}{r[1]:<32}{r[2]:<52}{r[3]}")

plt.tight_layout()
plt.show()