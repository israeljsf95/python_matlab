# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 13:48:33 2020

@author: israe
"""

import turtle

rodando = True

while rodando:
    print('Entre com triagulo, quadrado ou saida:')
    entrada = input()
    
    if entrada == 'triangulo':
        for i in range(3):
            turtle.forward(100)
            turtle.right(120)
    
    elif entrada == 'quadrado':
        for i in range(4):
            turtle.forward(100)
            turtle.right(90)
    
    elif entrada == 'saida':
        rodando = False
        print('exiting...')
    
    else:
        print('Comando não reconhecido')

print('Tchauzinho!')