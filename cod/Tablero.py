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
        rango = self.__rango
        if rango == 0:
            print ('No se puede generar un tablero con rango inválido')
        else:
            divs = rango//5
            for i in range(1,6):
                matriz = self.__tablero
                fila = []
                for j in range(1,6):
                    item = rd.randint((divs*(i-1)+1), divs*i)
                    while item in fila:
                        item = rd.randint((divs*(i-1)+1), divs*i)
                    fila.append(item)
                matriz[i-1] = fila
            matriz = matriz.T  
            matriz[2,2] = 0
            self.__tablero = matriz
     
    def marcar(self, num):
        if num > self.__rango or num < 1:
            print('Digite un número realista')
        else:
            if num in self.__tablero:
                self.__marcado[self.__tablero == num] = True
                self.__anterior = True
            else:
                self.__anterior = False
                
    def revisarHorizontal(self):
        matrix = self.__marcado
        for i in range(5):
            if False not in matrix[i]:
                return True
        return False
                    
    def revisarVertical(self):
        matrix = self.__marcado.T
        for i in range(5):
            if False not in matrix[i]:
                return True
        return False
  
    def revisarDiagonal(self):
        matriz = self.__marcado
        dia1 = []
        dia2 = []
        for i in range(5):
            dia1.append(matriz[i,i])
            dia2.append(matriz[4-i,i])
        if False not in dia2:
            return True
        elif False not in dia1:
            return True
        return False

    def revisarI(self):
        matriz = self.__marcado
        I = []
        for i in range(5):
            I.append(matriz[0,i])
            I.append(matriz[4,i])
            I.append(matriz[i,2])
            
        if False not in I:
            return True
        return False
    
    def revisarH(self):
        matriz = self.__marcado.T
        H = []
        for i in range(5):
            H.append(matriz[0,i])
            H.append(matriz[4,i])
            H.append(matriz[i,2])
            
        if False not in H:
            return True
        return False
        

    def revisarO(self):
        matriz = self.__marcado
        O = []
        for i in range(5):
            O.append(matriz[0,i])
            O.append(matriz[4,i])
            O.append(matriz[i,0])
            O.append(matriz[i,4])
        if False not in O:
            return True
        return False

    def revisarX(self):
        matriz = self.__marcado 
        X = []
        for i in range(5):
            X.append(matriz[i,i])
            X.append(matriz[4-i,i])
        if False not in X:
            return True
        return False

    def revisarZ(self):
        matriz = self.__marcado
        Z = []
        for i in range(5):
            Z.append(matriz[0,i])
            Z.append(matriz[4,i])
            Z.append(matriz[4-i,i])
            
        if False not in Z:
            return True
        return False

    def revisarN(self):
        matriz = self.__marcado
        N = []
        for i in range(5):
            N.append(matriz[i,i])
            N.append(matriz[i,0])
            N.append(matriz[i,4])
        if False not in N:
            return True
        return False
        
    def revisarT(self):
        matriz = self.__marcado
        T = []
        for i in range(5):
            T.append(matriz[0,i])
            T.append(matriz[i,2])
            
        if False not in T:
            return True
        return False

    def revisarFull(self):
        matriz = self.__marcado
        if False not in matriz:
            return True
        return False
    
    def revisarCumple(self, num):
        if num not in self.__tablero:
            print('Su cumpleaños no está en el tablero')
            return False
        iloc = self.__marcado[self.__tablero == num][0,0]
        if iloc == True:
            return True
        return False
        














