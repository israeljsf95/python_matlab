# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:53:45 2020

@author: israe
"""

ini_bal = float(input("Entre com o total investido: "))
anos = int(input("Entre com o numero de anos: "))
taxa = int(input("Entre com a taxa em %: "))

taxa = taxa/100

acum_interesse = 0.0

#Inicio do Processo de visualizacao para formatacao em tabela 
print("%4s%18s%10s%16s" % ("Ano","Balanco Inicial", 
                           "Interesse", "Balanco Final"))


#Rodar o script
for ano in range(1, anos+1):
  interesse = ini_bal*taxa
  fin_bal = ini_bal + interesse
  print("%4d%18.2f%10.2f%16.2f" % (ano, ini_bal, interesse, fin_bal))
  ini_bal = fin_bal
  acum_interesse += interesse


print("Balanco Final: $%0.2f" % fin_bal)
print("Interesse total ganho: $%0.2f" %acum_interesse)