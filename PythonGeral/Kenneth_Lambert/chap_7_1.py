# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:53:52 2020

@author: israe
"""

from turtle import Turtle, colormode
from polygons import square, hexagon, radialPattern
import random

colormode(255)

def desenhar_pad(t, x, y, count, length, shape):
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.down()
    t.fillcolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    radialPattern(t, count, length, shape)
    t.end_fill()
    

def main():
    t = Turtle()
    t.speed(0)
    cont = 10
    largura = t.screen.window_width() // 2
    altura = t.screen.window_height() // 2
    tamanho = 30
    inseto = tamanho * 2
    desenhar_pad(t, -largura + inseto, altura - inseto, cont, tamanho, square)
    desenhar_pad(t, -largura + inseto, inseto - altura, cont, tamanho, square)
    tamanho = 20
    inseto = tamanho * 3
    desenhar_pad(t, largura - inseto, altura - inseto, cont, tamanho, hexagon)
    desenhar_pad(t, largura - inseto, inseto - altura, cont, tamanho, hexagon)
    
if __name__ == "__main__":
    main()
    
    