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
        self.__num = num
        self.__rango = rango
        self.__tableros = []
        self.__revisiones = revisiones
        self.__salidos = []
      
    @property
    def salidos(self):
        return self.__salidos
    
    @property
    def tableros(self):
        return self.__tableros
    
    @property
    def rango(self):
        return self.__rango
    
    @property
    def num(self):
        return self.__num
    
    @property
    def revisiones(self):
        return self.__revisiones
    
    @salidos.setter
    def salidos(self, new_salidos):
        self.__salidos = new_salidos
    
    @revisiones.setter
    def revisiones(self, new_revisiones):
        self.__revisiones = new_revisiones
    
    @tableros.setter
    def tablero(self, new_tableros):
        self.__tableros = new_tableros
      
    @rango.setter
    def rango(self, new_rango):
        self.__rango = new_rango
    
    @num.setter
    def rango(self, new_num):
        self.__num = new_num
    
    def __str__(self):
        return f'Colección de tableros \nRango: {self.__rango} \nNumero de tableros: {self.__num} \nTipo de revisiones: {self.__revisiones} \nNúmeros salidos: {self.__salidos}' 
    
    
    def construir(self):
        numero = self.__num
        for i in range(numero):
            tablero = tbl(self.__rango)
            tablero.generar()
            self.__tableros.append(tablero)
            
    def reset(self):
        if self.__tableros == []:
            print("Construya los valores primero")
        else:
            numero = self.__num
            for i in range(numero):
                self.__tableros[i].marcado = np.matrix([[False,False,False,False,False],
                                                        [False,False,False,False,False], 
                                                        [False,False,True,False,False], 
                                                        [False,False,False,False,False], 
                                                        [False,False,False,False,False]])
    
    def revisar(self):
        revisar = self.__revisiones
        for i in range(self.__num):
            if 'Horizontal' in revisar:
                boolean = self.__tableros[i].revisarHorizontal()
                if boolean:
                    # print(f'El tablero {i} ha ganado por la combinación Horizontal')
                    return True
            
            if 'Vertical' in revisar:
                boolean = self.__tableros[i].revisarVertical()
                if boolean:
                    # print(f'El tablero {i} ha ganado por la combinación Vertical')
                    return True
            
            if 'Diagonal' in revisar:
                boolean = self.__tableros[i].revisarDiagonal()
                if boolean:
                    # print(f'El tablero {i} ha ganado por la combinación Diagonal')
                    return True
            
            if 'H' in revisar:
                boolean = self.__tableros[i].revisarH()
                if boolean:
                    # print(f'El tablero {i} ha ganado por la combinación tipo H')
                    return True
            
            if 'I' in revisar:
                boolean = self.__tableros[i].revisarI()
                if boolean:
                    # print(f'El tablero {i} ha ganado por la combinación tipo H')
                    return True
                        
            if 'O' in revisar:
                boolean = self.__tableros[i].revisarO()
                if boolean:
                    # print(f'El tablero {i} ha ganado por la combinación tipo O')
                    return True
            
            if 'X' in revisar:
                boolean = self.__tableros[i].revisarX()
                if boolean:
                    # print(f'El tablero {i} ha ganado por la combinación tipo X')                    
                    return True
            
            if 'Z' in revisar:
                boolean = self.__tableros[i].revisarZ()
                if boolean:
                    # print(f'El tablero {i} ha ganado por la combinación tipo Z')
                    return True
            
            if 'N' in revisar:
                boolean = self.__tableros[i].revisarN()
                if boolean:
                    # print(f'El tablero {i} ha ganado por la combinación tipo N')
                    return True
            
            if 'T' in revisar:
                boolean = self.__tableros[i].revisarT()
                if boolean:
                    # print(f'El tablero {i} ha ganado por la combinación tipo T')
                    return True
            
            if 'Full' in revisar:
                boolean = self.__tableros[i].revisarFull()
                if boolean:
                    # print(f'El tablero {i} ha ganado por tablero lleno')
                    return True
            
            if 'Cumple' in revisar:
                boolean = self.__tableros[i].revisarCumple()
                if boolean:
                    # print(f'El tablero {i} ha ganado por marcar su cumpleaños')
                    return True
        return False
    
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
            
    def simular_juego(self):
        a = self
        boolean = False
        while boolean == False:
            self.num_random()
            boolean = a.revisar()
            if boolean:
                return len(self.__salidos)
            
            
            
            
           
            
            
            