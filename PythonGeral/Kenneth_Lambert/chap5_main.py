# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:33:48 2020

@author: israe
"""
"""
Brincando com as mains

"""



def quadrado(x):
    return x*x

def main():
    numero = float(input("Entre com um numero: "))
    print("O quadrado de ", numero, " e: ", quadrado(numero))
    


if __name__ == "__main__":
    main()