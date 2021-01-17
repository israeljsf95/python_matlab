# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:40:06 2020

@author: israe
"""

#Testando minhas habilidades de modelagem com nupy 

import matplotlib.pyplot as plt
import numpy as np
from const_models_pinv import fourier

f = 2
w = 2*np.pi*f

t = np.linspace(0, 4, 200)
tamos = t[1] - t[0]
x = np.sin(t*w)
v = np.random.normal(0, 0.1, x.size)
y = x + v 
A = fourier(t, f, 1)
theta = np.linalg.pinv(A).dot(y)
y_model = A.dot(theta)

fig, ax = plt.subplots(nrows = 2, ncols = 1, figsize = (5,5))

ax[0].plot(t,y)
ax[0].plot(t, y_model)
ax[0].set_ylabel('y(t)')
ax[0].legend(['y_ruido','y_modelo'], loc = 'upper right')


ax[1].plot(t, x)
ax[1].plot(t, y_model)
ax[1].set_xlabel('tempo(s)')
ax[1].set_ylabel('y(t)')
ax[1].legend(['x_s_ruido','y_modelo'], loc = 'upper right')
plt.show()

EQM1 = ((y_model-y)**2).sum()/(y.size)
EQM2 = ((y_model-x)**2).sum()/(y.size)
print(f'Erro Quadratico Medio entre o sinal ruidoso e a filtragem por LSQ: {EQM1:.2f}')
print(f'Erro Quadratico Medio entre a filtragem e o sinal original: {EQM2:.2f}')


