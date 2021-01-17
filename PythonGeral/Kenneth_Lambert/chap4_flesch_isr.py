# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:57:01 2020

@author: israe

Programa que calcula o indice de Flesch
"""

nome_arquivo = input("Entre com o nome do arquivo: ")
arquivo_entrada = open(nome_arquivo, 'r')
text = arquivo_entrada.read()

#contar as frases
cont_frases = text.count('.') + text.count('?') + text.count(':') + text.count(';') + text.count('!')

#contar as palavras
cont_palavras = len(text.split())
cont_silabas = 0
vogais = "aeiouAEIOU"

#parte necessaria para contar as coisas de acordo com o indice de Flesch
for palavra in text.split():
  for vogal in vogais:
    cont_silabas += palavra.count(vogal)
  for final in ['es', 'ed', 'e']:
    if palavra.endswith(final):
      cont_silabas -= 1
  if palavra.endswith('le'):
    cont_silabas += 1

#calculando o indice
indice_flesch = 206.835 - 1.015*(cont_palavras/cont_frases) - 84.6*(cont_silabas/cont_palavras)
nivel = round(0.39*(cont_palavras/cont_frases) + 11.8*(cont_silabas/cont_palavras) - 15.59) 

print("O indice de Flesch e: ",indice_flesch)
print("O nível da escolaridade e: ", nivel)
print("Numero de Frases: ", cont_frases)
print("Numero de Palavras: ", cont_palavras)
print("Numero de Silabas: ", cont_silabas)   

