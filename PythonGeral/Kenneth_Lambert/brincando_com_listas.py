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
print()
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
print()
print("A mediana e: ", end = " ")
if len(lista) % 2 == 1:
    print(lista[ponto_medio])
else:
    print((lista[ponto_medio] + lista[ponto_medio-1])/2)
        


print()
print("O valor medio dos primeiros 100 numeros ao quadrado e: ", soma/len(lista))



#melhor forma de percorrer uma lista e atraves de enumerate
#pois garantimos o argumento do for nao passara ou gerara erro
#de acesso 



print('\nConstruindo a lista de cores: ')
cores = ['vermelho','laranja','amarelo']

for indice, valor in enumerate(cores):
    print(f'{indice}: {valor}')

print()



numeros = [19, 3, 15, 7, 11]
print('Criando um grafico de barra a partir da lista numeros: ')
print(f'Indice {"Valor": >8}    Barras')

for indice, valor in enumerate(numeros):
    print(f'{indice: > 5}{valor: > 8}      {"*" * valor}')


lista_num = list(range(20))

lista_num_2 = [item**2 for item in lista_num]
lista_num_3 = [item**2 for item in lista_num if item % 2 == 0]
lista_num_4 = [item**3 for item in lista_num_3 if item % 3 == 0]

cores_maiusculas = [cor.upper() for cor in cores]


#Isso que faremos nao e uma lista, porem podemos acessa-lo depos
quadrado_num_imp = (x**2 for x in lista_num if x %2 != 0)

quadrado_num_imp = list(quadrado_num_imp)



print()

#brincando com filters, maps e Reduces
def impar(x):
    return x % 2 != 0

#filter tb retorna um objeto do tipo filter, logo para poder
#poder visualizar o resultado da funcao, precisamos
print(list(filter(impar,list(quadrado_num_imp))))
print()
#Outra forma de conseguir a mesma coisa
print([item for item in quadrado_num_imp if impar(item)])


#Usando expressoes lambda para subtituir funcoes
print()
print(list(filter(lambda x: x % 2 != 0, lista_num)))

print()
print(list(map(lambda x: x**2, lista_num)))


#combinando filtros com maps
print()
list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, lista_num)))

"""
Map aplica uma determinado funcao em um objeto iteravel e retorna um objeto do
tipo mapa

Filter aplica uma funcao predicado que e avaliado em True ou False, caso True o
objeto do tipo filter e incrementado e adicionado o elemento que compoem o obje
to iteravel. 

Reduce aplica uma funcao que recebe dois parametros e a aplica em um objeto ite
vel

"""
from functools import reduce

def soma(x,y): return x + y
def prod(x,y): return x * y

dado = list(range(1,5))
print("Dados: ", dado)
print()
print("A soma dos elementos em dados e: ", reduce(soma, dado))
print()
print("O produto dos elementos em dados e: ",reduce(prod, dado))


#Gente olha que foda isso

print(reduce(lambda x, y: x + y, dado))
print(reduce(lambda x, y: x * y, dado))


dict1 = {'1':'israel', '2':'renato', 
         '3':'junqueira', '4':'shyshy', '5':'tawan'}


