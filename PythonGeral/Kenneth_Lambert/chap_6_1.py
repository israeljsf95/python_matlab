# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:31:16 2020

@author: israe
"""
import os, os.path

SAIR = '7'
COMANDOS = ('1','2','3','4','5','6','7')
MENU = """ 1 Liste o diretorio atual
2 Subir
3 Descer
4 Numero de Aqruivos no Diretorio
5 Tamanho do Diretorio em bytes
6 Busque por um arquivo
7 Sair do Programa"""

def main():
    while True:
        print(os.getcwd())
        print(MENU)
        comando = aceitar_comando()
        executar_comando(comando)
        if comando == SAIR :
            print("Tenha um bom dia!")
            break
        

def aceitar_comando():
    comando = input("Entre com um numero: ")
    if comando in COMANDOS:
        return comando
    else:
        print("Erro: Comando nao reconhecido")
        return aceitar_comando()
    
def executar_comando(comando):
    if comando == '1':
        liste_dir_atual(os.getcwd())
    elif comando == '2': 
        subir()
    elif comando == '3' :
        descer(os.getcwd())
    elif comando == '4':
        print("O numero total de arquivos e: ", contar_arquivos(os.getcwd()))
    elif comando == '5':
        print("O numero total de bytes e: ", contar_bytes(os.getcwd()))
    elif comando == '6':
        alvo = input("Entre com uma string de busca: ")
        arq_lista = achar_arquivos(alvo, os.getcwd())
        if not arq_lista:
            print("String nao encontrada: ")
        else:
            for f in arq_lista:
                print(f)

def liste_dir_atual(dir_nome):
    lyst = os.listdir(dir_nome)
    for element in lyst: print (element)

def subir():
    os.chdir("..")
    
def descer(dir_atual):
    novo_dir = input("Entre com o nome do diretorio: ")
    if os.path.exists(dir_atual + os.sep + novo_dir) and os.path.isdir(novo_dir):
        os.chdir(novo_dir)
    else:
        print("Erro: nao existe diretorio com esse nome!")

def contar_arquivos(caminho):
    cont = 0
    lyst = os.listdir(caminho)
    for elemento in lyst:
        if os.path.isfile(elemento):
            cont += 1
        else:
            os.chdir(elemento)
            cont += contar_arquivos(os.getcwd())
            os.chdir("..")
    return cont


def contar_bytes(caminho):
    cont = 0
    lyst = os.listdir(caminho)
    for elemento in lyst:
        if os.path.isfile(elemento):
            cont += os.path.getsize(elemento)
        else:
            os.chdir(elemento)
            cont += contar_bytes(os.getcwd())
            os.chdir("..")
    return cont

def achar_arquivos(alvo, caminho):
    arquivos = []
    lyst = os.listdir(caminho)
    for elemento in lyst:
        if os.path.isfile(elemento):
            if alvo in elemento:
                arquivos.append(elemento)
            
    return arquivos


if __name__ == "__main__":
    main()
            













        