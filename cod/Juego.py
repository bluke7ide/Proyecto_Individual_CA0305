# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 18:40:40 2024

@author: PC01
"""

from Bingo import Bingo
import random as rd

class Juego():
    def __init__(self, sim, rango, num):
        self.__sim = sim
        self.__rango = rango
        self.__num = num
        
    @property
    def sim(self):
        return self.__sim
    
    @property
    def rango(self):
        return self.__rango
    
    @property
    def num(self):
        return self.__num
        
    @sim.setter
    def sim(self, new_sim):
        self.__sim = new_sim
    
    @num.setter
    def num(self, new_num):
        self.__num = new_num
      
    @rango.setter
    def rango(self, new_rango):
        self.__rango = new_rango
        
    def __str__(self):
        return f'Simulaciones: {self.__sim} \nRango: {self.__rango} \nNumero de tableros: {self.__tableros}' 
        
    def mean_salidos(sim, rango, tableros):
        proy = []
        for i in range(sim):
            a = Bingo(self.__num, rango, [''])
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