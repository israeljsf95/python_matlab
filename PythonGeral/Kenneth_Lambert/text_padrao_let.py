# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 16:42:04 2020

@author: israe
"""


n = int(input("Entre com o numero de linha: "))
o = ord('@')
for i in range(1,n+1):
    for j in range(1, n-i+1):
        print(end = " ")
    for j in range(i, 0, -1):
        print(chr(o+j), end = "")
    for j in range(2,i+1):
        print(chr(o+j), end = "")
    print()
        