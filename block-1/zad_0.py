import numpy as np  # Подключаем библиотеку NumPy для математических вычислений и работы с массивами
import matplotlib.pyplot as plt  # Подключаем модуль Matplotlib для построения графиков



A = 2  
f = 5  
phi = 0  


t = np.linspace(0, 1, 1000) 





u = A * np.sin(2 * np.pi * f * t + phi)





u_max = np.max(u)

u_min = np.min(u)


print("=" * 50)

print("ЗАДАНИЕ 0")

print("=" * 50)


print("\n1. Исходный сигнал")

print(f"Амплитуда A = {A} В")

print(f"Частота f = {f} Гц")

print(f"Начальная фаза φ = {phi} рад")


print(f"\nМаксимальное значение: {u_max:.2f} В")


print(f"Минимальное значение: {u_min:.2f} В")



T = 1 / f



number_of_periods = f * 1


print(f"\n2. Период сигнала:")
print(f"T = 1 / f = {T:.2f} с")


print(f"\nКоличество полных колебаний за 1 секунду:")
print(f"N = f × t = {number_of_periods:.0f}")




plt.figure(figsize=(10, 5))


plt.plot(t, u, label="u(t) = 2sin(2π·5t)")



plt.title("Исходный синусоидальный сигнал")


plt.xlabel("Время, с")


plt.ylabel("Амплитуда, В")


plt.grid(True)


plt.axhline(0, color="black", linewidth=0.8)


plt.axvline(0, color="black", linewidth=0.8)


plt.legend()


plt.tight_layout()


plt.show()



A1 = 1

A2 = 4


u_A1 = A1 * np.sin(2 * np.pi * f * t)


u_A2 = A2 * np.sin(2 * np.pi * f * t)


plt.figure(figsize=(10, 5))


plt.plot(t, u_A1, label="A = 1 В")


plt.plot(t, u_A2, label="A = 4 В")


plt.title("Изменение амплитуды")


plt.xlabel("Время, с")


plt.ylabel("Амплитуда, В")


plt.grid(True)


plt.axhline(0, color="black", linewidth=0.8)


plt.legend()


plt.tight_layout()


plt.show()


print("\n3. Изменение амплитуды:")

print("При A = 1 В колебания становятся в 2 раза меньше.")

print("При A = 4 В колебания становятся в 2 раза больше.")

print("Частота и период при этом не изменяются.")



frequencies = [2, 10, 20]


plt.figure(figsize=(10, 5))


for freq in frequencies:

    signal = A * np.sin(2 * np.pi * freq * t)

    plt.plot(t, signal, label=f"f = {freq} Гц")


plt.title("Изменение частоты")


plt.xlabel("Время, с")


plt.ylabel("Амплитуда, В")


plt.grid(True)


plt.axhline(0, color="black", linewidth=0.8)


plt.legend()


plt.tight_layout()


plt.show()



print("\n4. Изменение частоты:")


for freq in frequencies:

    period = 1 / freq

    cycles = freq * 1



    print(
        f"f = {freq:2} Гц: "
        f"T = {period:.3f} с, "
        f"колебаний за 1 с = {cycles:.0f}"
    )



phi_new = np.pi / 2



u_phi = A * np.sin(2 * np.pi * f * t + phi_new)


plt.figure(figsize=(10, 5))


plt.plot(t, u, label="φ = 0")


plt.plot(t, u_phi, label="φ = π/2")


plt.title("Изменение начальной фазы")


plt.xlabel("Время, с")


plt.ylabel("Амплитуда, В")


plt.grid(True)


plt.axhline(0, color="black", linewidth=0.8)


plt.legend()


plt.tight_layout()


plt.show()


print("\n5. Изменение начальной фазы:")

print("φ = 0 → сигнал начинается с нулевого значения.")


print("φ = π/2 → сигнал начинается с максимального значения +A.")


print("Изменение фазы приводит к горизонтальному сдвигу графика.")



max_indices = []



for i in range(1, len(u) - 1):

    if u[i] > u[i - 1] and u[i] > u[i + 1]:


        max_indices.append(i)


max_times = t[max_indices]


print("\n6. Расстояние между соседними максимумами:")


if len(max_times) >= 2:


    distances = np.diff(max_times)



    print("Временные координаты максимумов:")
    print(np.round(max_times, 3))


    print("\nРасстояния между соседними максимумами:")
    print(np.round(distances, 3))


    print(f"\nРасчётный период: {T:.3f} с")


    print(
        f"Среднее расстояние между максимумами: "
        f"{np.mean(distances):.3f} с"
    )





print("\n" + "=" * 50)
print("ИТОГ")
print("=" * 50)


print(f"Амплитуда исходного сигнала: {A} В")


print(f"Максимум: {u_max:.2f} В")


print(f"Минимум: {u_min:.2f} В")


print(f"Частота: {f} Гц")


print(f"Период: {T:.2f} с")


print(f"Количество колебаний за 1 с: {number_of_periods:.0f}")


print("При увеличении амплитуды меняется высота колебаний.")


print("При увеличении частоты увеличивается количество колебаний.")


print("При изменении фазы график сдвигается по горизонтали.")