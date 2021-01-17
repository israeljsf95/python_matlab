# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:50:28 2020

@author: israe
"""
import random
import numpy as np


N = 350
l1 = [random.randrange(1,11) for i in range(N)]
unique_l1, cont_vezes = np.unique(l1, return_counts = 'True')

print('Criando um grafico de barra a partir da lista numeros: ')
print(f'Indice {"Frequencia": >8}  Barras')

for indice, valor in zip(unique_l1, cont_vezes):
    print(f'{indice: > 5}{valor: > 8}      {"*" * valor}')
