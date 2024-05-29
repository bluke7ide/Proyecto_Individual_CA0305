# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:05:56 2024

@author: PC01
"""

import numpy as np
import random as rd

class Tablero():
  
    def __init__(self, rango):
        self.__tablero = np.matrix([[0,0,0,0,0],
                                    [0,0,0,0,0], 
                                    [0,0,0,0,0],
                                    [0,0,0,0,0],
                                    [0,0,0,0,0]])
        self.__marcado = np.matrix([[False,False,False,False,False],
                                    [False,False,False,False,False], 
                                    [False,False,True,False,False], 
                                    [False,False,False,False,False], 
                                    [False,False,False,False,False]])
        self.__anterior = False
        if (rango >= 25) and (rango % 5 == 0):
            self.__rango = rango
        else:
            print('El rango debe de ser mínimo 25 y calzar con las 5 líneas')
            self.__rango = 0
    
    @property
    def anterior(self):
        return self.__anterior
    
    @property
    def tablero(self):
        return self.__tablero
    
    @property
    def marcado(self):
        return self.__marcado
    
    @property
    def rango(self):
        return self.__rango
    
    @anterior.setter
    def anterior(self, new_anterior):
        self.__anterior = new_anterior
        
    @tablero.setter
    def tablero(self, new_tablero):
        self.__tablero = new_tablero
        
    @marcado.setter
    def marcado(self, new_marcado):
        self.__marcado = new_marcado
      
    @rango.setter
    def rango(self, new_rango):
        self.__rango = new_rango
      
    def __str__(self):
        return f'Tablero: \n{self.__tablero}\nMarcados: \n{self.__marcado} \nRango: {self.__rango}'

    def generar(self):
        divs = self.__rango//5
        for i in range(1,6):
            
            fila = []
            for j in range(1,6):
                item = rd.randint((divs*(i-1)+1), divs*i)
                while item in fila:
                    item = rd.randint((divs*(i-1)+1), divs*i)
                fila.append(item)
            self.__tablero[i-1] = fila
        self.__tablero = self.__tablero.T  
        self.__tablero[2,2] = 0
     
    def marcar(self, num):
        if num > self.__rango or num < 1:
            print('Digite un número realista')
        else:
            if num in self.__tablero:
                self.__marcado[self.__tablero == num] = True
                self.__anterior = True
            else:
                self.__anterior = False
    
    def revisar(self, tipo):
        array = []
        if 'Horizontal' == tipo:
            for i in range(5):
                if False not in self.__marcado[i]:
                    return True
            return False 
        
        elif 'Vertical' == tipo:
            for i in range(5):
                if False not in self.__marcado.T[i]:
                    return True
            return False  
        
        elif 'Diagonal' == tipo:
            dia1 = []
            dia2 = []
            for i in range(5):
                dia1.append(self.__marcado[i,i])
                dia2.append(self.__marcado[4-i,i])
            if False not in dia2 or False not in dia1:
                return True
            return False
        
        elif 'H' == tipo:
            for i in range(5):
                array.append(self.__marcado.T[0,i])
                array.append(self.__marcado.T[4,i])
                array.append(self.__marcado.T[i,2])
            if False not in array:
                return True
            return False
        
        elif 'I' == tipo:
            for i in range(5):
                array.append(self.__marcado[0,i])
                array.append(self.__marcado[4,i])
                array.append(self.__marcado[i,2])
            if False not in array:
                return True
            return False
                    
        elif 'O' == tipo:
            for i in range(5):
                array.append(self.__marcado[0,i])
                array.append(self.__marcado[4,i])
                array.append(self.__marcado[i,0])
                array.append(self.__marcado[i,4])
            if False not in array:
                return True
            return False
        
        elif 'X' == tipo:
            for i in range(5):
                array.append(self.__marcado[i,i])
                array.append(self.__marcado[4-i,i])
            if False not in array:
                return True
            return False
        
        elif 'Z' == tipo:
            for i in range(5):
                array.append(self.__marcado[0,i])
                array.append(self.__marcado[4,i])
                array.append(self.__marcado[4-i,i])
            if False not in array:
                return True
            return False
        
        elif 'N' == tipo:
            for i in range(5):
                array.append(self.__marcado[i,i])
                array.append(self.__marcado[i,0])
                array.append(self.__marcado[i,4])
            if False not in array:
                return True
            return False
        
        elif 'T' == tipo:
            for i in range(5):
                array.append(self.__marcado[0,i])
                array.append(self.__marcado[i,2])
            if False not in array:
                return True
            return False
        
        elif 'Full' == tipo:
             if False not in self.__marcado:
                 return True
             return False  
    
















