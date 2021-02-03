#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5 import QtWidgets
# Aca agrego estos 2
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt
import sys
import numpy as np
import math
import time
import Interfaz_resultados_B
# me traigo cada objeto creado
from class_Bolita_B import *

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# ahora tengo que meter estos objetos en MyWindow !!


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test del Trazo A Frame 1")
        print("2 - Creaste la ventana principal estas usando una funcion render")
        self.render()

    def render(self):

        layout = QVBoxLayout()

        # Crear Label Principal
        label1 = QLabel(
            "BIENVENIDO AL TEST_01 DIGITAL \n Aqui cargaremos los datos\n de los individuos \n Es el INPUT de la aplicacion")
        label1.setStyleSheet("background: green; color: yellow")
        # centrar el label dentro del QLabel
        label1.setAlignment(Qt.AlignCenter)

        # Crear entrada de texto

        self.user_input1 = QLineEdit()
        self.user_input1.setPlaceholderText("Nombre")
        self.user_input1.setClearButtonEnabled(True)

        self.user_input2 = QLineEdit()
        self.user_input2.setPlaceholderText("Apellido")
        self.user_input2.setClearButtonEnabled(True)

        self.user_input3 = QLineEdit()
        self.user_input3.setPlaceholderText("DNI")
        self.user_input3.setClearButtonEnabled(True)

        # Crear Label Secundario

        label2 = QLabel("Elija el nivel de escolaridad \n maximo alcanzado")
        label2.setStyleSheet("background: orange; color: blue")
        # Centrar el label dentro del QLabel
        label2.setAlignment(Qt.AlignCenter)

        # Crear Label_Opciones y Radio Button

        label_primario = QLabel(" Primario")
        R_bt1 = QRadioButton(self)
        # R_bt .move(10,260)

        label_secundario = QLabel(" Secundario")
        R_bt2 = QRadioButton(self)
        # R_bt .move(10,260)

        label_universitario = QLabel(" Universitario")
        R_bt3 = QRadioButton(self)
        # R_bt .move(10,260)

        # Crear los botones

        btn1 = QPushButton("Mostrar Info")
        # btn1.setGeometry(0, 100, 100 ,30)
        btn1.setStyleSheet("background: blue; color: red")

        btn2 = QPushButton("Enviar Data")
        # btn2.setGeometry(0, 130, 100 ,30)
        btn2.setStyleSheet("background: orange; color: blue")

        btn3 = QPushButton("Graficar Data")
        # btn3.setGeometry(0, 130, 100 ,30)
        btn3.setStyleSheet("background: brown; color: yelow")

        mensaje = "\n Este dato ha sido enviado por una señal (evento) y recibido por un slot(funcion handler)"

        grafico = "\n Aqui se grafican los  resultados del test"

        sms_pri = "\n Eligio como Nivel Educativo el PRIMARIO"

        sms_sec = "\n Eligio como Nivel Educativo el SECUNDARIO"

        sms_uni = "\n Eligio como Nivel Educativo el UNIVERSITARIO"

        # programar la señal de ambos botone
        # --> con connect tenemos que programar un slot (handler si o si) que pasa luego del click
        btn1.clicked.connect(self.slot1)
        btn2.clicked.connect(lambda: self.slot2(mensaje))
        btn3.clicked.connect(lambda: self.slot3(grafico))

        R_bt1.clicked.connect(lambda: self.slotP(sms_pri))
        R_bt2.clicked.connect(lambda: self.slotS(sms_sec))
        R_bt3.clicked.connect(lambda: self.slotU(sms_uni))

        # ---------------triggers ----------------------
        self.user_input1.returnPressed.connect(self.show_text_NA)
        self.user_input2.returnPressed.connect(self.show_text_NA)
        self.user_input3.returnPressed.connect(self.show_text_DNI)

        for widget in [label1, self.user_input1, self.user_input2, self.user_input3, label2, label_primario, R_bt1, label_secundario, R_bt2, label_universitario, R_bt3, btn1, btn2, btn3]:
            layout.addWidget(widget)

        widget = QWidget(self)
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def show_text_NA(self):
        print("El nombre y apellido del usuario es: ",
              self.user_input1.text(), self.user_input2.text())
        # el metodo .text es el que me trae el texto del QLineEdit

    def show_text_DNI(self):
        print("El Documento es: ", self.user_input3.text())

    def slot1(self):
        print("\n Lo que hace este slot-funcion es mostrar info con un print")

    def slot2(self, mensaje):  # slot con parametros y envio de datos
        # --> print("Apretaste el boton ese es el evento \n  y el slot o handler es lo que pasa cuando lo apretas \n lo que paso es un print en la shell")
        print(mensaje)

    def slot3(self, grafico):
        print(grafico)

    def slotP(self, sms_pri):
        print(sms_pri)

    def slotS(self, sms_sec):
        print(sms_sec)

    def slotU(self, sms_uni):
        print(sms_uni)


#####################
#####################


class MyWindow(QMainWindow):
    # Función de inicialización de nuestras variables
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 500, 530)
        self.setWindowTitle("Test de trazo tipo B")
        # se crea el atributo "rango" para poder recorrer mejor cada bolita
        self.rango = ["b1", "b2", "b3", "b4", "b5"]
        self.bolitas = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12,
                        b13, bl1, bl2, bl3, bl4, bl5, bl6, bl7, bl8, bl9, bl10, bl11, bl12]

        self.initUI()

    def initUI(self):

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Bienvenido al Test_01 Digital")
        self.label.move(50, 50)
        self.update()

        # Boton terminar
        self.b_Fin = QtWidgets.QPushButton(self)
        self.b_Fin.setText("Terminar")
        self.b_Fin.clicked.connect(self.terminar)
        self.b_Fin.move(400, 0)

        # Boton comenzar
        self.b_inicio = QtWidgets.QPushButton(self)
        self.b_inicio.setText("Comenzar")
        self.b_inicio.clicked.connect(self.comenzar)

        print("\n Estos objetos existen y son las bolitas")
        for i in range(len(self.bolitas)):
            self.bolitas[i].Obj = self.bolitas[i].t_Obj(self)
            self.bolitas[i].Obj.setGeometry(
                self.bolitas[i].g1, self.bolitas[i].g2, self.bolitas[i].g3, self.bolitas[i].g4)
            self.bolitas[i].Obj.setStyleSheet(self.bolitas[i].setStyleSheet)
            self.bolitas[i].Obj.clicked.connect(
                lambda ch, val=i: self.cambioColor(val))

    def clicked(self):
        self.label.setText("El tiempo corre")
        self.update()

    def cerrarSesion(self):
        self.label.setText("La evaluacion terminó")
        print("El tiempo final fue de :.... ")
        self.update()

    def update(self):
        self.label.adjustSize()

    def comenzar(self):
        # Macro de instrucciones al apretar el boton comenzar

        global bol_ini
        global bol_fin
        global bol_time
        global bol_time_ver
        global dist
        global tr
        global x_old
        global y_old

        bol_ini = []
        bol_fin = []
        bol_time = []
        bol_time_ver = [0]  # Tiempo de las bolitas verdes
        dist = [0]
        x_old = 0
        y_old = 0

        tr = np.zeros(25, dtype='int8')

        self.b_Fin.setText("Terminar")
        self.b_Fin.clicked.connect(self.terminar)
        self.clicked()     # responde ante el click
        self.guardar_ti()  # guarda el tiempo inicial
        self.bolilleroNumeros()  # reinicia la distribucion de numeros
        self.resetearColorTodos()

    def terminar(self):
        # Macro de instrucciones al apretar el boton terminar
        self.cerrarSesion()
        self.guardar_tf()
        self.guardar_dur()
        self.resultado()

    def resultado(self):
        # Macro de instrucciones al apretar el boton resultado

        global bol_ini
        global bol_fin
        global bol_time
        global dist

        self.b_Fin.setText("Resultados")
        self.b_Fin.clicked.disconnect()
        self.b_Fin.clicked.connect(lambda:
                                   self.resultado_mostrar(bol_ini, bol_fin, bol_time, bol_time_ver[1:], dist[1:]))

    def resultado_mostrar(self, ini, fin, tim, timv, dist):
        self.in_res = Interfaz_resultados_B.MyWindow()
        self.in_res.initUI(ini, fin, tim, timv, dist)
        self.in_res.show()

    def cambioColor(self, i):
        global numero_estado1
        global tr
        global dist
        global x_old
        global y_old
        orden = ['0', '1', 'A', '2', 'B', '3', 'C', '4', 'D', '5', 'E', '6',
                 'F', '7', 'G', '8', 'H', '9', 'I', '10', 'J', '11', 'K', '12',
                 'L', '13']

        if numero_estado1 + 1 == orden.index(self.bolitas[i].valor):
            self.bolitas[i].Obj.setStyleSheet(
                "background-color: green; color: white; border-radius : 15; border : 1px solid green")
            for x, e in enumerate(tr):
                if e == 1:
                    self.bolitas[x].t_Obj.setStyleSheet(
                        self.bolitas[x].setStyleSheet)
                    tr[x] = 0

            print("Color Verde")

            dist.append(math.sqrt(
                ((self.bolitas[i].g1 - x_old)**2) + ((self.bolitas[i].g2 - y_old)**2)))
            x_old = self.bolitas[i].g1
            y_old = self.bolitas[i].g2

            bol_time_ver.append(
                round((time.time() - inicio) - bol_time_ver[-1], 3))

        elif numero_estado1 < orden.index(self.bolitas[i].valor):
            print("Color Rojo")
            tr[i] = 1
            self.bolitas[i].Obj.setStyleSheet(
                "background-color: red; color: white; border-radius : 15; border : 1px solid red")

        else:
            print("Advertencia")
            print("Esta tecla ya se clickeó, vuelva a intentar")

        bol_ini.append(str(orden[numero_estado1]))
        bol_fin.append(str(self.bolitas[i].valor))
        bol_time.append(str(round(time.time() - inicio, 3)))
        if numero_estado1 + 1 == orden.index(self.bolitas[i].valor):
            numero_estado1 += 1



    def resetearColorTodos(self):
        global numero_estado1
        global tr
        global ta
        global rango

        for i in range(len(self.bolitas)):
            self.bolitas[i].Obj.setStyleSheet(self.bolitas[i].setStyleSheet)

        numero_estado1 = 0

        tr = np.zeros(25, dtype='int8')
        ta = np.zeros(25, dtype='int8')

        print("El contador se reseteo a ", numero_estado1)

    def bolilleroNumeros(self):
        global rango
        global n
        
        rrango = np.arange(1, 26)
        n = np.random.permutation(rrango)

        letras_o = ['A','B','C','D','E','F','G','H','I','J','K','L']

        for i in range(len(self.bolitas)):

            if n[i] <= 13:
                self.bolitas[i].valor = str(n[i])
                self.bolitas[i].Obj.setText(self.bolitas[i].valor)

            elif n[i] > 13:
                self.bolitas[i].valor = str(letras_o[n[i]-14])
                self.bolitas[i].Obj.setText(self.bolitas[i].valor)
        
        
        

     

        print("el orden de bolitas es", n)

    def guardar_ti(self):
        global current_time_1
        global inicio

        current_time_1 = time.strftime("%H:%M:%S")
        inicio = time.time()
        print("El tiempo inicial es: ", current_time_1)
        return current_time_1

    def guardar_tf(self):
        global current_time_2
        global final

        current_time_2 = time.strftime("%H:%M:%S")
        final = time.time()
        print("El tiempo final fue: ", current_time_2)
        return current_time_2

    def guardar_dur(self):
        global total
        global inicio
        global final
        global bol_ini
        global bol_fin
        global bol_time

        total = round(final - inicio, 3)
        print("El tiempo total fue de ", total, "segundos")
        print("El orden de bolitas fue de", bol_ini,
              "\n", bol_fin, "\n", bol_time)


# control del trazo
numero_estado1 = 0

# control de errores
tr = np.zeros(25, dtype='int8')
ta = np.zeros(25, dtype='int8')




if(__name__ == '__main__'):
    app = QApplication(sys.argv)
    win0 = MainApp()          # Se establece una ventana principal
    win0.show()
    win = MyWindow()
    win.show()
    print("La primere bolita tiene posicion", bl1.valor,"y su letra es: ", bl1.letra)
    print("La 2 bolita tiene posicion", bl2.valor,"y su letra es: ", bl2.letra)
    print("La 3 bolita tiene posicion", bl3.valor,"y su letra es: ", bl3.letra)
    sys.exit(app.exec())
