# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:05:56 2024

@author: PC01
"""

import numpy as np
import random as rd

class Tablero():
  
    def __init__(self, rango):
        '''
        Constructor de un tablero

        Parámetros
        ----------
        rango : int
            Rango del tablero.

        Retorna
        -------
        Nada.

        '''
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
            # El rango debe de ser adecuado para repartirse en las 5 columnas
            self.__rango = rango
        else:
            print('El rango debe de ser mínimo 25 y calzar con las 5 líneas')
            self.__rango = None 
       
    @property
    def tablero(self):
        ''' 
        Getter de tablero

        Retorna
        -------
        np.matrix
            Matriz con el tablero.

        '''
        return self.__tablero
    
    @property
    def marcado(self):
        ''' 
        Getter de marcado

        Retorna
        -------
        np.matrix
            Matriz con las casillas marcadas.

        '''
        return self.__marcado
    
    @property
    def anterior(self):
        ''' 
        Getter de anterior

        Retorna
        -------
        boolean
            Indicador del número pasado.

        '''
        return self.__anterior
    
    @property
    def rango(self):
        ''' 
        Getter de rango

        Retorna
        -------
        int
            Rango del tablero.

        '''
        return self.__rango
        
    @tablero.setter
    def tablero(self, new_tablero):
        ''' 
        Setter de tablero
        
        Parámetros
        ----------
        new_tablero : np.matrix
            Nueva matriz con el tablero.

        Retorna
        -------
        Nada.

        '''
        self.__tablero = new_tablero
        
    @marcado.setter
    def marcado(self, new_marcado):
        ''' 
        Setter de marcado
        
        Parámetros
        ----------
        new_marcado : np.matrix
            Nueva matriz con las casillas marcadas.

        Retorna
        -------
        Nada.

        '''
        self.__marcado = new_marcado
        
    @anterior.setter
    def anterior(self, new_anterior):
        ''' 
        Setter de anterior
        
        Parámetros
        ----------
        new_anterior : boolean
            Nuevo indicador del número pasado.

        Retorna
        -------
        Nada.

        '''
        self.__anterior = new_anterior
      
    @rango.setter
    def rango(self, new_rango):
        ''' 
        Setter de rango
        
        Parámetros
        ----------
        new_rango : int
            Rango nuevo del tablero.

        Retorna
        -------
        Nada.

        '''
        if (new_rango >= 25) and (new_rango % 5 == 0):
            self.__rango = new_rango
        else:
            print('El rango debe de ser mínimo 25 y calzar con las 5 líneas')
      
    def __str__(self):
        '''
        Función str del objeto Tablero

        Returns
        -------
        str
            El string que despliega algunos atributos.

        '''
        return f'''
                Tablero: 
                {self.__tablero}
                Marcados: 
                {self.__marcado} 
                Rango: {self.__rango}
                '''

    def generar(self):
        '''
        Función que genera los números en el tablero

        Returns
        -------
        None.

        '''
        if (self.__rango >= 25) and (self.__rango % 5 == 0): # Verificación
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
            self.__tablero[2,2] = 0 # El centro está marcado
        else:
            print('El rango debe de ser mínimo 25 y calzar con las 5 líneas')
        
     
    def marcar(self, num):
        '''
        Función que marca el número en el tablero, si es posible.

        Parameters
        ----------
        num : int
            Número a marcar

        Returns
        -------
        None.

        '''
        if num > self.__rango or num < 1:
            print('Digite un número realista')
        else:
            if num in self.__tablero:
                self.__marcado[self.__tablero == num] = True
                self.__anterior = True
            else: # Directamente no está
                self.__anterior = False
    
    def revisar(self, tipo):
        '''
        Función que revisa las combinaciones posibles

        Parameters
        ----------
        tipo : str
            String con la combinación. Puede ser
            Horizontal, Vertical, Diagonal, H, I, O, X, Z, N, T, o Full. 

        Returns
        -------
        boolean
            El caso que haya acertado la verificación.

        '''
        array = []
        # Aunque se repitan valores, lo importante es saber si son todos True
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
    
















