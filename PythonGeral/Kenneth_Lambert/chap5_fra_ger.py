# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 14:43:13 2020

@author: israe

Construindo um gerador de Frases em Ingles
"""
import random


#gerando os dicionarios de possibilidades

lista_art = ("A","THE")
lista_subst = ("BOY", "GIRL", "BAT", "BALL")
lista_verbos = ("HIT","SAW","LIKED")
lista_prep = ("WITH","BY")



def sentence():
    """"Constroi e retorna uma sentenca"""
    return frase_subst() + " " + frase_verb()  + "."

def frase_subst():
    "Constroi e  retorna uma  frase substantivada"
    return random.choice(lista_art) + " " + random.choice(lista_subst)

def frase_verb():
    return random.choice(lista_verbos) + " " + frase_subst() + " " + frase_prep()

def frase_prep():
    return random.choice(lista_prep) + " " + frase_subst()

def main():
    """Dizer para o usuario informar o numero de sentencas para gerar """
    numero = int(input("Entre com o numero de sentencas: "))
    for contador in range(numero):
        print(sentence())


if __name__ == "__main__":
    main()