# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 18:40:40 2024

@author: PC01
"""

from Bingo import Bingo
from Tablero import Tablero 
import random as rd

class Simulaciones():
    def __init__(self, sim, rango, num):
        self.__sim = sim
        self.__rango = rango
        self.__num = num
        
    @property
    def sim(self):
        '''
        Getter de sim

        Retorna
        -------
        int
            Número de simulaciones. Recomendado 100.

        '''
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
            proy.append(local.num_random(False))
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
        prob = cuentan/self.__sim
        return f'La prob simulada de que ganen dos o más tableros es {prob}'
    
    def mean_bolita(self):
        proy = []
        for j in range(self.__rango):
            proy.append([])
        for i in range(self.__sim):
            local = Bingo(self.__num, self.__rango, [''])
            local.construir()
            for j in range(self.__rango):
                proy[j].append(local.num_random(False))
        for j in range(self.__rango):    
            proy[j] = sum(proy[j])/len(proy[j])
        return proy
    
    def prob_cond(self):
        prob = []
        for i in range(24):
            prob.append([])
            for j in range(self.__rango-i):
                prob[i].append([])
                local = Tablero(75)
                local.generar()
                salidos = []
                num = rd.randint(1, self.__rango)
                for c in range(i):
                    while num in salidos or num not in local.tablero:
                        num = rd.randint(1, self.__rango)
                    local.marcar(num)
                num = rd.randint(1, self.__rango)
                for c in range(j-i):
                    while num in salidos or num in local.tablero:
                        num = rd.randint(1, self.__rango)
                
                
                for c in range(self.__sim):
                    num = rd.randint(1, self.__rango)
                    while num in salidos:
                        num = rd.randint(1, self.__rango)
                    prob[i][j].append(num in local.tablero)
                prob[i][j] = sum(prob[i][j])/self.__sim      
        return prob
    
    def mean_especifico(self, tipo):
        proy = []
        for i in range(self.__sim):
            local = Bingo(self.__num, 
                      self.__rango,
                      tipo)
            local.construir()
            proy.append(local.simular_juego(False)[0])
        mean = sum(proy)/len(proy)
        return f'La media simulada de que un tablero gane es {mean}'
            
    def prob_win(self, marcado, salidos):
        # Considera que tiene al menos una combinación con una bolita restante
        prob_tablero = 24/self.__rango
        prob_win = 1/(24-marcado) *(salidos+1)/24
        if marcado < 3 or self.__rango - salidos < 24 - marcado or marcado > salidos:
            return 0
        return prob_tablero*prob_win
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    