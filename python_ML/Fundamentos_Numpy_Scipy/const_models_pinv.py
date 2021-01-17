# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:48:05 2020

@author: israe
"""
import numpy as np


#funcoes para construir a matriz usada na PSEUDO-Inversao 

def fourier(x, f, n):
    #entrada é o tempo e f é a frequencia estimada do sinal
    x = x.flatten()
    A = np.zeros((x.size, 2*n + 1), dtype = float)
    for i in range(0,n,2):
        A[:, i] = np.sin(2*np.pi*(i+1)*f*x)
        A[:, i+1]= np.cos(2*np.pi*(i+1)*f*x)
    A[:,-1] = np.ones(x.size)
    return A
    

def polin(x, n):
    x = x.flatten()
    print('x.shape: ', x.shape)
    A = np.zeros((x.size, n), dtype = float)
    print('A.shape: ', A.shape)

    for i in range(0,n):
        A[:, (n-1)-i] = x**i
    return A