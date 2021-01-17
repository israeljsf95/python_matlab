a = 2
b = 4
c = a/b
print(a)

'''
brincano com os bitwise
'''
print(1 << 3)


#Alguns testes com strings

s1 = 'israel e legal'
#imprimindo um pedaco de s1
#do primeiro ao segundo carac
#tere
print(s1[0:2])

#imprimindo o tamanho de s1
print(len(s1))

#usando indexacao inversa
print(s1[-1])
print(s1[-len(s1)])


#Strings constituem um tipo que imutavel
#ou seja, a linha  de codigo abaixo gera
#ra um erro no interpretador
#s1[1] = 4

#Uma coisa interessante a se notar e que
#o operador slice (:) funciona como o matlab e o scilab
#Concatenando strings(sobrecarga de operadores)
s2 = s1 + s1

#para inserir uma string com diferentes tipos 
#de identificadores
s3 = "i'srael e o cara"
print(s3)


#brincando um pouco mais com as strings
#o comando format substitui nos locais
#indicados pelas chaves o que sera pos
#to nas chaves

print("Hoje eu estou {0} python e depois {1}".format('aprendendo', 'javascript'))
s4 = "Hoje eu estou {0} python e depois {1}"
print(s4.format('bunda', 'tristeza'))

print("precos: {x}, {y}, {z}".format(x = 1, y = 2, z = 3))

#for loops com range
#range(inicio, parada, passo)
#range itera do inicio ate parada-1
for i in range(10):#0 a 9
    print(i)

for i in range(2,10):#2 a 9
    print(i)

for i in range(2,10,2):#2 a 8 pois 9 nao e acessivel com passo 2
    print(i)


#Uma das melhores coisas em python 

for i in range(len(s3)):
    print(s3[i])

for char in s3:
    print(char)

#Empilhando for's
for i in range(3):
    for j in range(2):
        print(i,j)

#fazendo tabelinhas 10 x 10
for i in range(1,11):
   print('{:<3}|'.format(i), end='')
   for j in range(1,11):
      print('{:>4}'.format(i*j),end='')
   if i == 1:
     print('\n{:#^44}'.format(''), end = '')
   print('')

#while loops 
'''
while True:
    print('deu merda!!!')
'''


#condition e chamado de flag
#ele controla a execucao do 
#loop
condition = 10

while (condition != 0):
    print(condition)
    condition -=1

while (True):
    print('Achou errado Otario!!')
    break


#uso do comando continue

for i in range(10):
    if i == 5:
        continue
    print(i)


# Vamos construir funcoes hihihih

def function():
    print('Ola burro!')

def function2():
    return 'Ola burro!'

def function3():
    return 'Israel', 2


function()
f1 = function2()
print(type(function3())) #Caraca retorna  uma tupla, que sensacional
                         #porem retorna um objeto imutável e que ocu
                         #muito lugar na memoria, cuidado!!!

