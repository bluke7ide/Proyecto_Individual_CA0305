# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:29:28 2024

@author: PC01
"""

from Tablero import Tablero
import numpy as np
import random as rd

class Bingo():
    
    def __init__(self, num, rango, revisiones):
        ''' 
        Constructor de un juego de bingo

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
        self.__revisiones = revisiones
        self.__tableros = []
        self.__salidos = []
      
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
    
    @property
    def rango(self):
        ''' 
        Getter de rango

        Retorna
        -------
        int
            Rango de los tableros.

        '''
        return self.__rango
    
    @property
    def revisiones(self):
        ''' 
        Getter de revisiones

        Retorna
        -------
        list
            Lista con los tipos de revisiones.

        '''
        return self.__revisiones
    
    @property
    def tableros(self):
        ''' 
        Getter de tableros

        Retorna
        -------
        list
            Lista con los tableros.

        '''
        return self.__tableros
    
    @property
    def salidos(self):
        ''' 
        Getter de salidos

        Retorna
        -------
        list
            Lista con los números salidos.

        '''
        return self.__salidos
    
    
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
    
    @revisiones.setter
    def revisiones(self, new_revisiones):
        ''' 
        Setter de revisiones
        
        Parámetros
        ----------
        new_revisiones : list
            Lista nueva con los números salidos.

        Retorna
        -------
        Nada.

        '''
        self.__revisiones = new_revisiones    
    
    @tableros.setter
    def tableros(self, new_tableros):
        ''' 
        Setter de tableros
        
        Parámetros
        ----------
        new_tableros : list
            Lista nueva con los tableros.

        Retorna
        -------
        Nada.

        '''
        self.__tableros = new_tableros    

    @salidos.setter
    def salidos(self, new_salidos):
        ''' 
        Setter de salidos
        
        Parámetros
        ----------
        new_salidos : list
            Lista nueva con los números salidos.

        Retorna
        -------
        Nada.

        '''
        self.__salidos = new_salidos
    
    
    def __str__(self):
        '''
        Función str del objeto Bingo

        Retorna
        -------
        str
            El string que despliega algunos atributos

        '''
        return f'''
                Colección de tableros 
                Rango: {self.__rango} 
                Numero de tableros: {self.__num} 
                Tipo de revisiones: {self.__revisiones} 
                Números salidos: {self.__salidos}
                ''' 
    
    
    def construir(self):
        '''
        Función que construye los números en los tableros usando generar()

        Retorna
        -------
        Nada.

        '''
        for i in range(self.__num):
            tablero = Tablero(self.__rango)
            tablero.generar()
            self.__tableros.append(tablero)
            
    def reset(self):
        '''
        Función que devuelve todos los marcados al estado principal

        Retorna
        -------
        Nada.

        '''
        if self.__tableros == []:
            print("Construya los valores primero")
        else:
            self.__salidos = []
            for i in range(self.__num):
                self.__tableros[i].marcado = np.matrix([
                    [False,False,False,False,False],
                    [False,False,False,False,False], 
                    [False,False,True,False,False], 
                    [False,False,False,False,False], 
                    [False,False,False,False,False]
                ])
    
    def revisar(self, imprimir):
        '''
        Función que revisa si alguno de los tableros ha ganado

        Parámetros
        ----------
        imprimir : boolean
            Si el usuario desea imprimir el ganador

        Retorna
        -------
        win : int
            Cantidad de tableros ganadores

        '''
        if self.__tableros == []:
            print("Construya los valores primero")
        else:
            win = 0
            for i in range(self.__num):
                for j in self.__revisiones:
                    if(self.__tableros[i].revisar(j)):
                        win += 1 # múltiples ganadores
                        if imprimir:
                            print(
                                f'El tablero {i+1} ganó por la combinación {j}'
                            )        
            return win
    
    def num(self, numero):
        '''
        Función que marca el número específico en los tableros

        Parámetros
        ----------
        numero : int
            Número a marcar

        Returns
        -------
        cuenta : int
            Tableros que han logrado marcar el número.

        '''
        if self.__tableros == []:
            print("Construya los valores primero")
        elif numero in self.__salidos:
            print("Ese número ya salió")
        else:
            cuenta = 0
            for i in range(self.__num):
                self.__tableros[i].marcar(numero)
                if (self.__tableros[i].anterior):
                    cuenta = cuenta + 1
            self.__salidos.append(numero)
            return cuenta
    
    def num_random(self, imprimir):
        '''
        Función que a partir de randint escoge un número a marcar y lo marca

        Parámetros
        ----------
        imprimir : boolean
            Si el usuario desea imprimir el número que sale
            
        Retorna
        -------
        Nada.

        '''
        num = rd.randint(1, self.__rango)
        while num in self.__salidos:
            num = rd.randint(1, self.__rango)
        if imprimir:
            print(f'El numero {num} ha salido')
        return self.num(num) 
            
    def simular_juego(self, imprimir):
        '''
        Función que simula un juego de bingo

        Parámetros
        ----------
        imprimir : boolean
            Si el usuario desea imprimir el ganador

        Retorna
        -------
        int
            La cantidad de bolitas que se tardó para ganar

        '''
        if self.__tableros == []:
            print("Construya los valores primero")
        else:
            win = 0
            while win == 0:
                self.num_random(False)
                win = self.revisar(imprimir)
            return len(self.__salidos), win
    
            
            
            
           
            
            
            