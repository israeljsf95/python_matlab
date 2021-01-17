# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 23:18:42 2020

@author: israe
"""

decimal = int(input("Entre com inteiro decimal: "))
if decimal == 0:
  print(0)
else:
  print("Quociente      Resto         Binario")
  bit_str = ""
  while decimal > 0:
    resto = decimal % 2
    decimal = decimal // 2 #pega a parte inteira do quociente
    bit_str = str(resto) + bit_str
    print("%6d%12d%19s" % (decimal, resto, bit_str))

print("A representacao em binario e: ", bit_str)