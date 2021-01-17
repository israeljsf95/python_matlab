# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:20:13 2020

@author: israe
"""

#Abrindo, escrevendo e salvando arquivos em python
"""
Caso o arquivo seja aberto em um ambiente com a biblioteca os
aberta vai precisar de uma flag para poder criar, ler e modificar 
arquivo a ser processado no diretorio, 
"""


import random
import os


#esta funcao aqui e sensacional
def unique(x):
  
  u = []
  
  for elemento in x:
    if elemento not in u:
      u.append(elemento)
  
  return u 


#funcao para buscar todos os arquivos com extensao em 
#determinado caminho
  
def extrair_nome_arq(arquivos, caminho):
  #pega os arquivos no caminho
  lista_arquivos_caminho= os.listdir(caminho)
  lista_selecionados = []
  for nome in lista_arquivos_caminho:
    for ext in arquivos:
      if ext in nome:
        lista_selecionados.append(nome)
        
  return lista_selecionados
      




f = open("arq_teste.txt",'w')


for cont in range(500):
  numero = random.randint(1, 500)
  f.write(str(numero) + '\n')

f.close()


#lendo as coisas que foram escritas

f = open("arq_teste.txt",   'r')

leitura_arq = f.read()
list_arq = leitura_arq.split()
unicos_em_leitura_list_arq = unique(list_arq)

#contando quantas vezes cada elemento aconteceu leitura_arquivo

soma = []
for elemento in unicos_em_leitura_list_arq:
  soma.append(leitura_arq.count(elemento))


ext = [".py", ".m"]
caminho = "D:\\Bibliotecas_Usuario\\Documentos\\Documentos\\UFS\\Estudo de Computação\\python_matlab\\Kenneth_Lambert"

print(extrair_nome_arq(ext, caminho))



