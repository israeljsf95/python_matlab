# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 12:57:39 2020

@author: israe
"""

#Programinha para calcular a qnt media de letras em uma determinada
#frase



frase = input('Entre com uma frase: ')

lista_palavra = frase.split()
tam_lista = len(lista_palavra)
soma_letras = 0
for palavra in lista_palavra:
  soma_letras += len(palavra)

print("A media de letras na frase e: %.2f" %(soma_letras/tam_lista))