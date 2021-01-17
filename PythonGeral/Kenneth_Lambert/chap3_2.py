# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:12:01 2020

@author: israe
"""

soma  = 0 

dados = input("Entre com um numero ou digite enter para sair: ")
while dados != "":
  numero = float(dados)
  soma += numero
  dados = input("Entre com um numero ou digite enter para sair: ")
  
print("A soma é", soma)

#Agora soma com for ou com while

soma = 0

for cont in range(1,100001):
  soma += cont
print(soma)



soma = 0
cont = 1

while (cont <= 100000):
  soma += cont
  cont += 1
print(soma)


#brincando com o break 

while True:
  numero = int(input("Entre  com um numero: "))
  if (numero >= 0) and (numero <=100):
    break
  else: 
    print("Error: numero tem que estar entre 0 e 100")
print(numero)    
