# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 18:40:40 2024

@author: PC01
"""

from Bingo import Bingo
import random as rd

class Simulaciones():
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
        return f'''
                Número de simulaciones: {self.__sim} 
                Rango: {self.__rango} 
                Numero de tableros: {self.__tableros}
                ''' 
        
    def mean_salidos(self):
        proy = []
        for i in range(self.__sim):
            local = Bingo(self.__num, self.__rango, [''])
            local.construir()
            proy.append(local.num(rd.randint(1,self.__rango)))
            print(i)
        mean = sum(proy)/len(proy)
        return f'La media simulada de que los tableros marquen es {mean}'
        
    def mean_normal(self):
        proy = []
        for i in range(self.__sim):
            local = Bingo(self.__num, 
                      self.__rango,
                      ['Horizontal', 'Vertical', 'Diagonal'])
            local.construir()
            proy.append(local.simular_juego(False)[0])
            print(i)
        mean = sum(proy)/len(proy)
        return f'La media simulada de que un tablero gane es {mean}'
    
    def prob_mas_1(self):
        cuentan = 0
        for i in range(self.__sim):
            local = Bingo(self.__num, 
                      self.__rango,
                      ['Horizontal', 'Vertical', 'Diagonal'])
            local.construir()
            if local.simular_juego(False)[1] != 1:
                cuentan +=1
            print(i)
        prob = cuentan/self.__sim
        return f'La prob simulada de que ganen dos o más tableros es {prob}'
    