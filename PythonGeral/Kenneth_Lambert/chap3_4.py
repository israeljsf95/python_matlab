# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 18:30:15 2020

@author: israe
"""

import math 

x = float(input("Entre com um numero positivo: "))

tol = 1e-6

estimacao = 1 

while True:
  estimacao = (estimacao + x/estimacao)/2
  erro = abs(x - estimacao**2)
  if erro <= tol:
    break

print("Raiz Quadrada Estimada: %2.2f" % estimacao)
print("Raiz Quadrada pelo Python: %2.2f" % math.sqrt(x))


#metodo de Leibniz para estimar pi

inter = int(input("Entre com o numero de iteracoes: "))

apro_pi = 0
cont = 1
cont_f = 0
while True:
  if cont % 2 == 0:
    apro_pi += 1/cont
  else:
    apro_pi += -1/cont
  cont += 2
  cont_f +=  1
  if cont_f == inter :
    break
  

print("O valor de pi aproximado pelo metodo de leibniz e: %2.4f" % apro_pi)