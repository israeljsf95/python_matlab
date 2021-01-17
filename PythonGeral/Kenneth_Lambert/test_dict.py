# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:45:15 2020

@author: israe
"""



lista = ['mae', 'mae', 'mae', 'israel', 'israel', 'luisa', 'luisa', 'ivan']


dictio = {}

for nome in lista:
    numero = dictio.get(nome, None)
    if numero == None:
        dictio[nome] = 1
    else:
        dictio[nome] = numero + 1


maximo = max(dictio.values())

for chave in dictio:
    if dictio[chave] == maximo:
        print("A moda e: ", chave)
        break