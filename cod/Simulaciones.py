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
        '''
        Getter de rango

        Retorna
        -------
        int
            Número de simulaciones. Recomendado 100.

        '''
        return self.__rango
    
    @property
    def num(self):
        ''' 
        Getter de num

        Retorna
        -------
        int
            Número de tableros.

        '''
        return self.__num
        
    @sim.setter
    def sim(self, new_sim):
        ''' 
        Setter de sim
        
        Parámetros
        ----------
        new_sim : int
            Número nuevo de simulaciones. Recomendado 100.

        Retorna
        -------
        Nada.

        '''
        self.__sim = new_sim
    
    @rango.setter
    def rango(self, new_rango):
        ''' 
        Setter de rango
        
        Parámetros
        ----------
        new_rango : int
            Rango nuevo de los tableros.

        Retorna
        -------
        Nada.

        '''
        self.__rango = new_rango
    
    @num.setter
    def num(self, new_num):
        ''' 
        Setter de num
        
        Parámetros
        ----------
        new_num : int
            Nuevo número de tableros.

        Retorna
        -------
        Nada.

        '''
        self.__num = new_num
      
   
        
    def __str__(self):
        '''
        Función str del objeto Simulaciones

        Retorna
        -------
        str
            El string que despliega algunos atributos

        '''
        return f'''
                Número de simulaciones: {self.__sim} 
                Rango: {self.__rango} 
                Numero de tableros: {self.__tableros}
                ''' 
        
    def mean_salidos(self):
        '''
        Función que calcula la media de tableros que logran marcar una bolita
        que sale, por medio de simulaciones

        Retorna
        -------
        str
            Da la media. Se puede cambiar a entregar solo mean

        '''
        proy = []
        for i in range(self.__sim):
            local = Bingo(self.__num, self.__rango, [''])
            local.construir()
            proy.append(local.num_random(False))
        mean = sum(proy)/len(proy)
        return f'La media simulada de que los tableros marquen es {mean}'
        
    def mean_normal(self):
        '''
        Función que calcula la media de bolitas que tienen que salir
        para que un tablero gane, dadas las combinaciones 
        'Horizontal', 'Vertical' y 'Diagonal', por medio de simulaciones

        Retorna
        -------
        str
            Da la media. Se puede cambiar a entregar solo mean

        '''
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
        '''
        Función que calcula la probabilidad que dos tableros o más coincidan
        ganando un juego, dadas las combinaciones 
        'Horizontal', 'Vertical' y 'Diagonal', por medio de simulaciones

        Retorna
        -------
        str
            Da la probabilidad. Se puede cambiar a entregar solo prob

        '''
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
        '''
        Función que calcula la media de coincidencias por bolita en los 
        tableros. Note que deberían de ser independientes, puesto obviando
        la información pasada, todas las bolitas deberían de tener una cantidad
        similar de casillas para marcar. Sí, gaste el tiempo para ver eso.

        Retorna
        -------
        proy : list
            Lista de probabilidades por bolita

        '''
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
        '''
        Función que calcula la probabilidad condicional a que en el tablero, 
        habiendo marcado una cantidad de casillas, pueda marcar la siguiente
        bolita. 

        Returns
        -------
        prob : list
            Probabilidad de que se marque condicionado a la cantidad de bolitas

        '''
        prob = []
        for i in range(24):
            prob.append([])
            for j in range(self.__rango-24 + i):
                prob[i].append([])
                local = Tablero(75)
                local.generar()
                salidos = []
                num = rd.randint(1, self.__rango)
                for c in range(i+1):
                    while num in salidos or num not in local.tablero:
                        num = rd.randint(1, self.__rango)
                    local.marcar(num)
                    salidos.append(num)
                num = rd.randint(1, self.__rango)
                for c in range(j-i):
                    while num in salidos or num in local.tablero:
                        num = rd.randint(1, self.__rango)
                    salidos.append(num)
                
                for c in range(self.__sim):
                    num = rd.randint(1, self.__rango)
                    while num in salidos:
                        num = rd.randint(1, self.__rango)
                    prob[i][j].append(num in local.tablero)
                prob[i][j] = sum(prob[i][j])/self.__sim  
                
            print(i)
        return prob
    
    def mean_especifico(self, tipo):
        '''
        Función que calcula la media de bolitas que tienen que salir
        para que un tablero gane, dadas las combinaciones cualquier 
        combinación posible, por medio de simulaciones

        Retorna
        -------
        str
            Da la media. Se puede cambiar a entregar solo mean

        '''
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
        '''
        Función que simula una probabilidad de ganar al siguiente turno. 
        Hace muchos supuestos, pero aunque esté incorrecto, se aproxima a la 
        probabilidad real. 

        Retorna
        -------
        float
            La probabilidad de ganar al siguiente turno/bolita.

        '''
        # Considera que tiene al menos una combinación con una bolita restante
        prob_tablero = 24/self.__rango
        prob_win = 1/(24-marcado) *(salidos+1)/24
        if marcado < 3 or self.__rango - salidos < 24 - marcado or marcado > salidos:
            return 0
        return prob_tablero*prob_win
