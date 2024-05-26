# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 18:40:40 2024

@author: PC01
"""

from Bingo import Bingo
import random as rd


def mean_salidos(sim, rango, tableros):
    proy = []
    for i in range(sim):
        a = Bingo(tableros, rango, [''])
        a.construir()
        proy.append(a.num(rd.randint(1,rango)))
        print(i)
    mean_salidos = sum(proy)/len(proy)
    return f'La media simulada de que los tableros no marquen es {mean_salidos}'
    
def mean_normal(sim, rango, tableros):
    proy = []
    for i in range(sim):
        a = Bingo(tableros, rango, ['Horizontal', 'Vertical', 'Diagonal'])
        a.construir()
        proy.append(a.simular_juego())
        print(i)
    mean_normal = sum(proy)/len(proy)
    return f'La media simulada de que un tablero gane es {mean_normal}'