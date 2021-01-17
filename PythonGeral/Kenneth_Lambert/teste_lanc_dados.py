# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:33:12 2020

@author: israe
"""

import matplotlib.pyplot as plt
import numpy as np
import random 
import seaborn as sns



M = 100000 #numero de lancamentos
lancamentos = [random.randrange(1,7) for i in range(M)]
valores, frequencias = np.unique(lancamentos, return_counts = True)
titulo = f'Lancameno de Dado de Seis Lados {len(lancamentos):,} Vezes'
sns.set_style("whitegrid")
eixos = sns.barplot(valores, frequencias, palette = 'bright')
eixos.set_title(titulo)
eixos.set(xlabel = 'Valor do Dado', ylabel = 'Frequencia')
eixos.set_ylim(top = max(frequencias) * 1.1)

for bar, frequencia in zip(eixos.patches, frequencias):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    #text = f'{frequencia: ,}\n{frequencia/len(lancamentos):.2%}'
    eixos.text(text_x, text_y, None, fontsize = 11, ha = 'center', va = 'bottom')