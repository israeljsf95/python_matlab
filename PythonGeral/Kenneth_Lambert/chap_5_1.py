# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

#brincando com as listas

exemplos = [4, 2, 10, 8]
copia_direta = []
copia_inversa = []
print(exemplos)

for exemplo in exemplos:
    copia_direta.append(exemplo)

for exemplo in range(-1,-len(exemplos) - 1, -1):
    copia_inversa.append(exemplos[exemplo])

print(copia_direta)
print(copia_inversa)


#brincando de calcular a media

lista = [x**2 for x in range(1,100)]

soma = 0

"""
Podemos usar 'in' para verificar coisas que estao dentro de um determinado obje
to iteravel. Com isso certos tipos de verificacoes se tornam muito mais faceis
de serem feitas.


"""

#calculando o valor medio de lista
for num in lista:
    soma += num
    
#Calcunado a mediana
lista.sort()
ponto_medio = len(lista)//2 #pegando a parte inteira do quociente
print("A mediana e: ", end = " ")
if len(lista) % 2 == 1:
    print(lista[ponto_medio])
else:
    print((lista[ponto_medio] + lista[ponto_medio-1])/2)
        



print("O valor medio dos primeiros 100 numeros ao quadrado e: ", soma/len(lista))