import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = '/Users/sofiakanukova/Downloads/killme.xlsx'
xl = pd.ExcelFile(file)
data = xl.parse('voltage5', skiprows=1, usecols='B:D')
n = len(data)
x = []
y = []
v = []

for i in range(n):
    a = int(data['x, cm'].iloc[i])
    x.append(int(data['x, cm'].iloc[i]))
    a = int(data['y, cm'].iloc[i])
    y.append(int(data['y, cm'].iloc[i]))
    a = int(data['phi, V'].iloc[i])
    v.append(float(data['phi, V'].iloc[i]))

V = np.zeros((9, 9))

for i in range(9):
    for j in range(9):
        V[i, j] = v[9*i+j] - 0.5

lvl = np.linspace(-0.25, 0.25, 50)

plt.contour(V.T, cmap ='plasma', origin='lower', levels=lvl, extent=[-4.5, 4.5, -4.5, 4.5])
plt.colorbar()
plt.xlabel('X, cm')
plt.ylabel('Y, cm')
plt.title('Equipotential lines, Phi = 1 V')
plt.show()
