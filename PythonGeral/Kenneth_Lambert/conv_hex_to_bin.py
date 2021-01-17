# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:35:18 2020

@author: israe
"""

#Conversor hexa para binario


hex_to_BT = {'0':'0000', '1':'0001', '2':'0010',
             '3':'0011', '4':'0100', '5':'0101',
             '6':'0110', '7':'0111', '8':'1000',
             '9':'1001', 'A':'1010', 'B':'1011',
             'C':'1100', 'D':'1101', 'E':'1110',
             'F':'1111'}


def convert_hex_bin(numero, tabela):
    binario = ""
    for digito in numero:
        binario = tabela[digito] + binario
    return binario

