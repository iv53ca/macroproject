import numpy as np
import matplotlib.pyplot as plt

def cm_to_inch(value):
    return value/2.54

# Задание параметров
r = 0.5 # Радиус круговых электродов
L = 3.5 # Размер области
N = 100 # Количество точек на оси x и y
h = L / (N-1) # Шаг сетки
x = np.linspace(0, L, N)
y = np.linspace(0, L, N)

# Создание сетки и начальных условий
X, Y = np.meshgrid(x, y)
V = np.zeros((N, N))

# Определение расстояния до круговых электродов
r1 = 0.1*L
r2 = 0.9*L

# Задание граничных условий на границе области
for i in range(N):
    for j in range(N):
        if i == 0 or i == N-1 or j == 0 or j == N-1:
            V[i,j] = 0.0
        elif np.sqrt((X[i, j]-r1)**2 + (Y[i, j]-L/2)**2) < r:
            V[i,j] = 20.0
        elif np.sqrt((X[i, j]-r2)**2 + (Y[i, j]-L/2)**2) < r:
            V[i, j] = -20.0

V_old = V.copy()  # Текущее решение
V_new = V.copy()  # Новое решение

tol = 1e-2  # Порог точности
delta = 1  # Изменение решения на текущей итерации

# Решение уравнения Лапласа методом конечных разностей
while delta > tol:
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if np.sqrt((X[i, j]-r1)**2 + (Y[i, j]-L/2)**2) >= r and np.sqrt((X[i, j]-r2)**2 + (Y[i, j]-L/2)**2) >= r:
                V_new[i, j] = 0.25 * (V_old[i - 1, j] + V_old[i + 1, j] + V_old[i, j - 1] + V_old[i, j + 1])
    delta = np.max(np.abs(V_new - V_old)) # Оценка изменения решения на текущей итерации
    V_old = V_new.copy()  # Обновление текущего решения

# Итерационно решаем уравнение
# c = 0.5
# for k in range(100):
#     # Используем метод конечных разностей для нахождения лапласиана
#     laplacian = (np.roll(V_old, 1, axis=0) + np.roll(V_old, -1, axis=0)
#                  + np.roll(V_old, 1, axis=1) + np.roll(V_old, -1, axis=1)
#                  - 2*V_old) / h**2 + (np.roll(V_old, 1, axis=0)
#                  + np.roll(V_old, -1, axis=0) + np.roll(V_old, 1, axis=1) + np.roll(V_old, -1, axis=1)-2*V_old) / h**2
#     # Обновляем значение функции phi
#     V_old += 0.1 * (c*V_old - laplacian)


# Визуализация результатов
lvl = np.linspace(-20, 20, 2) # Задание контуров

plt.imshow(V_new.T, cmap='coolwarm', origin='lower', extent=[0, L, 0, L], aspect=1)
plt.colorbar()
plt.contour(V_new.T, cmap='seismic', origin='lower', levels=lvl, extent=[0, L, 0, L])
plt.colorbar()
plt.figure(figsize=(cm_to_inch(20), cm_to_inch(20)))

plt.show()