# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 16:59:25 2020

@author: israe
"""

#Entendendo o numpy e  o simpy junto com algumas 
#funcionalidades do matplotlib.pyplopt


import numpy as np



n = 100
arr1 = np.arange(1,n+1)
arr2 = np.linspace(0, 1, 100)
arr3 = np.logspace(0, 1, 100, base = 10)
cubo = np.ones((3,3,3)).astype(np.float16)


arr4 = np.arange(0,100).astype(int)
arr5 = np.arange(1000)
arr6 = arr5.reshape((10,10,10))


print(arr1.shape)
print(arr2.shape)

print(arr1.dot(arr2))


#Quando queremos utilizar as  ferramentas de algebra linear.
#Ao multiplicarmos as coisas como matrizes, farcilita o processo

A = np.matrix([[3,6,-5],
               [1,-3,2],
               [5,-1,4]])
B = np.matrix([[12],
               [-2],
               [10]])

X = A**(-1)*B
print(X)

#fazendo a mesma coisa com numpy array

a = np.array([[3,6,-5], #vetor coluna
              [1,-3,2], #vetor coluna
              [5,-1,4]]) #vetor coluna

b  = np.array([12,-2,10])#vetor coluna
bb = np.array([[12],[-2],[10]])

#Ou seja, para transpor é usar os metodos de transposição para
#facilitar a cabeca
x = np.linalg.inv(a).dot(b)
print(x)


from scipy.optimize import curve_fit

def func(x,a,b):
    return a*x + b

x = np.linspace(0,10, 100)
a = 1
b = 2
y = func(x,a,b)

yn = y + .9*np.random.normal(size=len(x))

popt, pcov = curve_fit(func, x, yn)
print(f'Parametros originais: a = {a}, b = {b} \nParametros Estimados: beta1 = {popt[0]:.2f}, beta2 = {popt[1]:.2f}')


m  = np.array([0, 1, 2, 3, 4])

M = [m+(i*10) for i in range(0, len(m) + 1)]
M = np.array(M)
print(M)


A = M
B = np.copy(M)
A[0,0] = 20
B[1,1] = 30

import matplotlib.pyplot as plt
from scipy import *
import scipy.linalg  as la
from scipy.special import jn, yn, jn_zeros, yn_zeros



x = np.linspace(0,10,200)


fig, ax = plt.subplots()

for n in range(5):
    ax.plot(x, jn(n, x), label =( r"$J_%d(x)$"%n))
ax.legend()


A = np.arange(10,19).reshape((3,3))
print('A: \n', A)


B = np.copy(A)
print('B: \n', B)

C = B[:,0] #pegando só a primeira coluna de B

print('C: \n', C)

#Aqui eu tenho o produto interno entre as linhas de A por C
print('A dot C: \n', A.dot(C))

#Aqui eu tenho o produto interno entre as colunas de A por C
print('C dot A: \n', C.dot(A))


#versao elegante para percorrer um array sem usar for no python


print('Media das Colunas: \n', np.apply_along_axis(np.mean, axis = 0, arr = A))
print('Media das Linhas: \n', np.apply_along_axis(np.mean, axis = 1, arr = A))
'''
Ou seja axis = 0 tira a media de cada vetor coluna em A
ja axis = 1 tira a media de cada linha coluna   
Este metodo tb e valido para funcoes proprias
'''

#Algo mais semelhante ao matlab para fazer extracoes de dados

A = np.random.random((4,4))

print('A: \n', A)

B = A[A < 0.5]
print('B = A < 0.5: \n', B)

A = np.ones((3,3))

B = np.zeros((3,3))

#Empilhando matrizes verticalmente
print(np.vstack((A,B)))

#Empilhando matrizes horizontalmente
print(np.hstack((A,B)))


#empilhando vetores
a = np.array([0,1,2])
b = np.array([3,4,5])
c = np.array([6,7,7])

#Empilha cada vetor como coluna 
print(np.column_stack((a, b, c)))

#empilha cada vetor como linha
print(np.row_stack((a, b, c)))

















