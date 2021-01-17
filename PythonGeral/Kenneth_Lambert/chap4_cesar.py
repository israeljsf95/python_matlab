# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 22:42:45 2020

@author: israe
"""

"""
A funcao ord('char') do python retorna o indice do char na tabela ASCII
enquanto que char(idx) retorna o caractere associado ao indice char na 
tabela ASCII 

"""


#Metodo de criptogradia de Cesar

texto_base = input("Entre com uma palavra minuscula: ")
dist = int(input("Entre com a distancia: "))
texto_base.lower()


#codificacao
codigo = ""
for char in texto_base:
  ord_val= ord(char)
  cifra_val = ord_val + dist
  if cifra_val > ord('z'):
    cifra_val = ord('a') + dist - (ord('z') - ord_val + 1)
  codigo += chr(cifra_val)

#decodificacao
decode = ""
for char in codigo:
  ord_val= ord(char)
  cifra_val = ord_val - dist
  if cifra_val < ord('a'):
    cifra_val = ord('z') + dist -  (ord('z') - ord_val + 1)
  decode += chr(cifra_val)



print("Palavra: " + texto_base)
print("Palavara Codificacao_Cesar: " + codigo + ". \nDistancia: " + str(dist))
print("Palavara De_Codificacao_Cesar: " + decode)

