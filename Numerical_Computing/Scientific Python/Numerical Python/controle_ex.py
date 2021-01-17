# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:58:06 2020

@author: israe

Exemplo usando o ferramental de Controle do Python
semelhante ao Matlab
"""

import os
import matplotlib.pyplot as plt   # MATLAB plotting functions
from control.matlab import *  # MATLAB-like functions

# Parameters defining the system
m = 250.0           # system mass
k = 40.0            # spring constant
b = 60.0            # damping constant

# System matrices
A = [[0, 1.], [-k/m, -b/m]]
B = [[0], [1/m]]
C = [[1., 0]]
sys = ss(A, B, C, 0)

# Step response for the system
plt.figure(1)
yout, T = step(sys)
plt.grid()
plt.title('Resposta do Sistema')
plt.xlabel('tempo(s)')
plt.plot(T.T, yout.T)
plt.show(block=False)

# Bode plot for the system
plt.figure(2)
mag, phase, om = bode(sys, logspace(-2, 2), Plot=True)
plt.show(block=False)
