# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:29:28 2024

@author: PC01
"""

from Tablero import Tablero as tbl
import numpy as np
import random as rd

class Bingo():
    
    def __init__(self, num, rango, revisiones):
        ''' Constructor de un juego de bingo

        Parametros
        ----------
        num : int
            Número de tableros.
        rango : int
            Rango de los tableros.
        revisiones : list
            Lista con los tipos de revisiones.

        Retorna
        -------
        Nada.

        '''
        self.__num = num
        self.__rango = rango
        self.__tableros = []
        self.__revisiones = revisiones
        self.__salidos = []
      
    @property
    def salidos(self):
        ''' Getter de salidos

        Retorna
        -------
        list
            Lista con los números salidos.

        '''
        return self.__salidos
    
    @property
    def tableros(self):
        ''' Getter de tableros

        Retorna
        -------
        list
            Lista con los tableros.

        '''
        return self.__tableros
    
    @property
    def rango(self):
        ''' Getter de rango

        Retorna
        -------
        int
            Rango de los tableros.

        '''
        return self.__rango
    
    @property
    def num(self):
        ''' Getter de num

        Retorna
        -------
        int
            Número de tableros.

        '''
        return self.__num
    
    @property
    def revisiones(self):
        ''' Getter de revisiones

        Retorna
        -------
        list
            Lista con los tipos de revisiones.

        '''
        return self.__revisiones
    
    @salidos.setter
    def salidos(self, new_salidos):
        self.__salidos = new_salidos
    
    @revisiones.setter
    def revisiones(self, new_revisiones):
        self.__revisiones = new_revisiones
    
    @tableros.setter
    def tableros(self, new_tableros):
        self.__tableros = new_tableros
      
    @rango.setter
    def rango(self, new_rango):
        self.__rango = new_rango
    
    @num.setter
    def num(self, new_num):
        self.__num = new_num
    
    def __str__(self):
        return f'''
                Colección de tableros 
                Rango: {self.__rango} 
                Numero de tableros: {self.__num} 
                Tipo de revisiones: {self.__revisiones} 
                Números salidos: {self.__salidos}
                ''' 
    
    
    def construir(self):
        for i in range(self.__num):
            tablero = tbl(self.__rango)
            tablero.generar()
            self.__tableros.append(tablero)
            
    def reset(self):
        if self.__tableros == []:
            print("Construya los valores primero")
        else:
            numero = self.__num
            for i in range(numero):
                self.__tableros[i].marcado = np.matrix([
                    [False,False,False,False,False],
                    [False,False,False,False,False], 
                    [False,False,True,False,False], 
                    [False,False,False,False,False], 
                    [False,False,False,False,False]
                ])
    
    def revisar(self, imprimir):
        if self.__tableros == []:
            print("Construya los valores primero")
        else:
            win = False
            for i in range(self.__num):
                for j in self.__revisiones:
                    if(self.__tableros[i].revisar(j)):
                        win = True # múltiples ganadores
                        if imprimir:
                            print(
                                f'El tablero {i+1} ganó por la combinación {j}'
                            )        
            return win
    
    def num(self, numero):
        if self.__tableros == []:
            print("Construya los valores primero")
        elif numero in self.__salidos:
            print("Ese número ya salió")
        else:
            cuenta = 0
            for i in range(self.__num):
                self.__tableros[i].marcar(numero)
                if (self.__tableros[i].anterior == False):
                    cuenta = cuenta + 1
            self.__salidos.append(numero)
            return cuenta
    
    def num_random(self):
        num = rd.randint(1, self.__rango)
        while num in self.__salidos:
            num = rd.randint(1, self.__rango)
        # print(f'El numero {num} ha salido')
        self = self.num(num)            
            
    def simular_juego(self, imprimir):
        if self.__tableros == []:
            print("Construya los valores primero")
        else:
            a = self
            boolean = False
            while boolean == False:
                self.num_random()
                boolean = a.revisar(imprimir)
            return len(self.__salidos)
    
            
            
            
           
            
            
            