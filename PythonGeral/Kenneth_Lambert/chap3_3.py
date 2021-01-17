# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:20:28 2020

@author: israe

Brincando com numeros aleatorios
"""


import random

#lancamento do dado 
for dado in range(10):
  print(random.randint(1,6), end = " ")
  


menor = int(input("Entre com um numero pequeno: "))
grande = int(input("Entre com um numero grande: "))
meu_numero = random.randint(menor, grande)
cont = 0
while True:
  cont+=1
  use_num = int(input("Entre com seu numero: "))
  if use_num < meu_numero:
    print("Muito Pequeno!")
  elif use_num > meu_numero:
    print("Muito Grande!")
  else:
    print("Parabéns! Voce conseguiu em", cont, "tentativas!")
    break
      
N = int(input("Entre com o Numero para o fatorial: "))
fat = 1
while (N > 1):
  fat = fat*N*(N-1)
  N = N-2
print(fat)


#testando a matematica

from math import log, round


N = int(input("Entre com o numero para calcular o log: "))
M = 0
while( (N % 2) != 0):
  M += 1
print("Logaritmo de N aproximado e: $", M, "o valor original e: $", round(log(N,2)))

  