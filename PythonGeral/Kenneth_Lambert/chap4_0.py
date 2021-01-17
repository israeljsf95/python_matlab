# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 22:32:32 2020

@author: israe
"""


#Importante e bem cabuloso a abstracao do Python
lis_arquivos = ["meu_pc.exe","menu.txt","jogos.txt","mnist.tar"]
ext = '.txt'

for nome in lis_arquivos:
  if ext in nome:
    print(nome)