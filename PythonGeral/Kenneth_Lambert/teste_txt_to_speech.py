# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 07:41:23 2020

@author: israe
"""

import os
import tkinter as tk
from gtts import gTTS
from playsound import playsound

janela = tk.Tk()
janela.title("Texto_fala")
janela.geometry("200x70")

def texto_to_fala():
  text = entrada.get()
  fala = gTTS(text = text, lang = "pt-br")
  
  fala.save('som.mp3')
  playsound('som.mp3')
  os.remove('som.mp3')
  
label = tk.Label(janela, text = "Entre aqui: ")
label.grid(row = 0, column = 0)

entrada = tk.Entry(janela)
entrada.grid(row = 1, column = 0)

botao = tk.Button(janela, text = 'Vai', command = texto_to_fala)
botao.grid(row = 1, column = 1)

janela.mainloop()