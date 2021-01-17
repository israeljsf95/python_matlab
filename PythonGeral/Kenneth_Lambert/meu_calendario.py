# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:14:41 2020

@author: israe
Meu proprio calendario
"""
import tkinter as tk
from tkinter import *
import calendar

janela = Tk()
janela.title("Calendario_Israel")


def text():
  month_str = mes.get()
  year_str = ano.get()  
  month_int = int(month_str)
  year_int = int(year_str)
  cal = calendar.month(year_int, month_int)
  campo_texto.delete(0.0, END)
  campo_texto.insert(INSERT, cal)

label1 = Label(janela, text = "Mes: ")
label1.grid(row = 0, column = 0)
mes = Spinbox(janela, from_ = 1, to = 12, width = 5)
mes.grid(row = 1, column = 0)



label2 = Label(janela, text = "Ano: ")
label2.grid(row = 0, column = 1)
ano = Spinbox(janela, from_ = 1700, to = 3000, width = 12)
ano.grid(row = 1, column = 1)

botao = Button(janela, text = "Vai", command = text)
botao.grid(row = 1, column = 2)

campo_texto = Text(janela, height = 8,  width = 22)
campo_texto.grid(row = 3, columnspan = 3)


janela.mainloop()