#!/usr/bin/env python
# coding: utf-8

# In[1]:

'''
linea 12: importamos desde PyQt5 (libreria para hacer interfaz grafica), la clase QtWidgets --> herramientas graficas
linea 13: de la libreria PyQt5 "capitulo" QWidgets -->  	QApplication (aplicacion) - QMainWindow - ventana principal de funcionamiento
linea 16: importar numpy (libreria de numeros y matrices o arreglos) as  (llamala como )
'''

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
#from PyQt5.QtCore import Qt

import numpy as np
#import sys
#import time

'''
linea 25: declaro una variable con el nombre n, digo que es una variable global
linea 26: una variable rango se le asigna (=)  un metodo-funcion "arange" de la libreria numpy
linea 27: que a la variable n le ponga los 25 valores desordenados de la variable rango
'''

global n
rango=np.arange(1,26)
n= np.random.permutation(rango)



##  Creo una segunda Clase
'''
linea 36: st es una variable que tiene asignada una funcion--> palabracoloreada() string
'''
st= str("border-radius : 15; border : 1px solid black")
#global st


'''
linea 44: declaramos y creamos una clase Bolitas
'''

class Bolitas():
    """ Aqui crearemos cada una de las bolitas del test
      con sus atributos y sus metodos para trabajarlas como objetos"""
    def __init__(self, setGeometry , t_Obj = QtWidgets.QPushButton, id = 0, valor = 0, estado = 0, setStyleSheet = st):
        #super(Bolitas, self).__init__()
        """ Create a new point at the origin """
        
        
        self.g1 = setGeometry[0] #Coordenada X
        self.g2 = setGeometry[1] #Coordenada Y
        self.g3 = setGeometry[2] #Anchura
        self.g4 = setGeometry[3] #Altura
        self.t_Obj= QtWidgets.QPushButton
        self.id = id
        self.valor = valor # puede tomar valores del 1 al 25
        self.estado = estado   # puede tener 3 estados Blanca,  Verde o Roja
        self.setStyleSheet = st

        
        


class BolitasLetras(Bolitas):
	def __init__(self, setGeometry ,letra, t_Obj = QtWidgets.QPushButton, id = 0, valor = 0, estado = 0, setStyleSheet = st):
		super().__init__(setGeometry , t_Obj, id, valor, estado, setStyleSheet)
		self.letra = letra
		
		#Bolitas.__init__(self, setGeometry , t_Obj = QtWidgets.QPushButton, id = 0, valor = 0, estado = 0, setStyleSheet = st)
		
	

       
        
print("Me parece que cree la primer bolita")
#print("Este es n: ", n)

i= 0

numero_estado1   = 0
numero_estado2   = 0
numero_estado3   = 0
numero_estado4   = 0
numero_estado5   = 0
numero_estado6   = 0
numero_estado7   = 0
numero_estado8   = 0
numero_estado9   = 0
numero_estado10 = 0
numero_estado11 = 0
numero_estado12 = 0
numero_estado13 = 0
numero_estado14 = 0
numero_estado15 = 0
numero_estado16 = 0
numero_estado17 = 0
numero_estado18 = 0
numero_estado19 = 0
numero_estado20 = 0
numero_estado21 = 0
numero_estado22 = 0
numero_estado23 = 0
numero_estado24 = 0
numero_estado25 = 0


# Creamos una bolita (25-bolitas) ahora como objeto de la clase Bolitas

b1 =    Bolitas([400,400,30,30], QtWidgets.QPushButton, "1" , n[0], 0, st)
b2 =    Bolitas([460,480,30,30], QtWidgets.QPushButton, "2" , n[1], 0, st)
b3 =    Bolitas([250,450,30,30], QtWidgets.QPushButton, "3" , n[2], 0, st)
b4 =    Bolitas([450,370,30,30] , QtWidgets.QPushButton, "4" , n[3], 0, st)
b5 =    Bolitas([250,50,30,30], QtWidgets.QPushButton, "5" , n[4], 0, st)
b6 =    Bolitas([20,470,30,30], QtWidgets.QPushButton, "6" , n[5], 0, st)
b7 =    Bolitas([380,200,30,30], QtWidgets.QPushButton, "7" , n[6], 0, st)
b8 =    Bolitas([200,200,30,30] , QtWidgets.QPushButton, "8" , n[7], 0, st)
b9 =    Bolitas([250,350,30,30] , QtWidgets.QPushButton, "9" , n[8], 0, st)
b10 =   Bolitas([180,280,30,30] , QtWidgets.QPushButton, "10", n[9], 0, st)
b11 =   Bolitas([130,420,30,30], QtWidgets.QPushButton, "11", n[10],0, st)
b12 =   Bolitas([420,130,30,30] , QtWidgets.QPushButton, "12", n[11],0, st)
b13 =   Bolitas([200,90,30,30] , QtWidgets.QPushButton, "13", n[12],0, st)


bl1 =    BolitasLetras([330,290,30,30],"A", QtWidgets.QPushButton, "1" , n[13], 0, st)

bl2 =    BolitasLetras([150,370,30,30], "B",QtWidgets.QPushButton, "2" , n[14], 0, st)
bl3 =    BolitasLetras([380,80,30,30],"C", QtWidgets.QPushButton, "3" , n[15], 0, st)
bl4 =    BolitasLetras([325,200,30,30] ,"D", QtWidgets.QPushButton, "4" , n[16], 0, st)
bl5 =    BolitasLetras([270,300,30,30],"E", QtWidgets.QPushButton, "5" , n[17], 0, st)
bl6 =    BolitasLetras([20,180,30,30],"F", QtWidgets.QPushButton, "6" , n[18], 0, st)
bl7 =    BolitasLetras([35,320,30,30],"G", QtWidgets.QPushButton, "7" , n[19], 0, st)
bl8 =    BolitasLetras([90,360,30,30],"H", QtWidgets.QPushButton, "8" , n[20], 0, st)
bl9 =    BolitasLetras([95,140,30,30],"I", QtWidgets.QPushButton, "9" , n[21], 0, st)
bl10 =   BolitasLetras([70,220,30,30],"J", QtWidgets.QPushButton, "10", n[22], 0, st)
bl11 =   BolitasLetras([180,150,30,30],"K", QtWidgets.QPushButton, "11", n[23],0, st)
bl12 =   BolitasLetras([135,80,30,30],"L",QtWidgets.QPushButton, "12", n[24],0, st)


print("La primere bolita tiene posicion", bl1.valor,"y su letra es: ", bl1.letra)
print("La 2 bolita tiene posicion", bl2.valor,"y su letra es: ", bl2.letra)
print("La 3 bolita tiene posicion", bl3.valor,"y su letra es: ", bl3.letra)
print("La 4 bolita tiene posicion", bl4.valor,"y su letra es: ", bl4.letra)
print("La 5 bolita tiene posicion", bl5.valor,"y su letra es: ", bl5.letra)
print("La 6 bolita tiene posicion", bl6.valor,"y su letra es: ", bl6.letra)
print("La 7 bolita tiene posicion", bl7.valor,"y su letra es: ", bl7.letra)
print("La 8 bolita tiene posicion", bl8.valor,"y su letra es: ", bl8.letra)
print("La 9 bolita tiene posicion", bl9.valor,"y su letra es: ", bl9.letra)
print("La 10 bolita tiene posicion", bl10.valor,"y su letra es: ", bl10.letra)
print("La 11 bolita tiene posicion", bl11.valor,"y su letra es: ", bl11.letra)
print("La 12 bolita tiene posicion", bl12.valor,"y su letra es: ", bl12.letra)
print("APRENDIMOS A USAR NUESTRA PRIMERA HERENCIA DE CLASES!! BRAVO")


'''vectorbolitas = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12,b13, bl1, bl2, bl3, bl4, bl5, bl6, bl7, bl8, bl9, bl10, bl11, bl12]
#i=10

def mostrarBolita():
	i=10
	if vectorbolitas[i]<14:
		print("muestro una bolita numerica")
	elif 14<vectorbolitas[i]<26:
		print("muestro una bolita de letra") 
		
	
mostrarBolita()
'''
