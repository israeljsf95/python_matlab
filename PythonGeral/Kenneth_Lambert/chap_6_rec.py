# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 18:51:10 2020

@author: israe
"""

def displayRange(lower, upper):
    
    if lower <= upper:
        print(lower)
        displayRange(lower+1, upper)
        


def soma(lower, upper):
    if lower>upper:
        print("Entrei no caso base!!!")
        return 0
    else:
        print("Entrando nas chamadas Recursivas!!!")
        return lower + soma(lower+1, upper)
    
    
def soma_rec_trace(lower, upper, margin):
    branco = " "*margin 
    print(branco,lower, upper)
    if lower > upper:
        print(branco, 0)
        return 0
    else:
        result = lower + soma_rec_trace(lower+1, upper, margin + 4)
        print(branco, result)
        return result
    
def fib(n):
    if n < 3:
        return 1
    else:
        print(fib(n-1) + fib(n-2))
        return fib(n-1) + fib(n-2)