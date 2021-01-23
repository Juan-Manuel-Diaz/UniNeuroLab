#!/usr/bin/env python
# coding: utf-8
# In[1]:

from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout,
                             QLabel, QLineEdit, QPushButton, QWidget, QAction)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import sys
import Interfaz_trazo


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login de credenciales")
        self.credenciales()

    def credenciales(self):
        centralwidget = QWidget()
        self.setCentralWidget(centralwidget)
        layout = QVBoxLayout(centralwidget)
        Bienvenida_lbl = QLabel("Bienvenidos a UniNeuroLab.\n \
            Favor de iniciar sesión para poder guardar sus estudios correctamente")
        Bienvenida_lbl.setAlignment(Qt.AlignCenter)
        user_input1 = QLineEdit()
        user_input1.setPlaceholderText("Nombre")
        user_input1.setClearButtonEnabled(True)

        user_input2 = QLineEdit()
        user_input2.setPlaceholderText("Apellido")
        user_input2.setClearButtonEnabled(True)

        user_input3 = QLineEdit()
        user_input3.setPlaceholderText("DNI")
        user_input3.setClearButtonEnabled(True)

        btn1 = QPushButton("Iniciar sesión")
        btn1.clicked.connect(lambda: self.user(
            user_input1.text(), user_input2.text()))
        btn2 = QPushButton("Entrar como anónimo")
        btn2.clicked.connect(self.Anon_User)

        layout.addWidget(Bienvenida_lbl)
        layout.addWidget(user_input1)
        layout.addWidget(user_input2)
        layout.addWidget(user_input3)
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        self.setLayout(layout)
        self.show()

    def Anon_User(self):
        self.main_menu = MainMenu()
        self.main_menu.show()
        self.close()

    def user(self, nombre, apellido):
        self.name = "{}, {}".format(apellido, nombre)
        self.main_menu = MainMenu(self.name)
        self.main_menu.show()
        self.close()


class MainMenu(QMainWindow):
    def __init__(self, name=None):
        super().__init__()
        self.setWindowTitle("UniNeuroLab - Menú Principal")
        self.setGeometry(100, 100, 800, 600)
        if name is None:
            self.name = "Anónimo/a"
        else:
            self.name = name

        self.UI()

    def UI(self):
        centralwidget = QWidget()
        self.setCentralWidget(centralwidget)
        layout = QVBoxLayout(centralwidget)

        lbl1 = QLabel(
            "Bienvenido a UniNeuroLab {}.\n Disfrute su visita".format(self.name))
        lbl1.setFont(QFont('Arial', 25))
        lbl1.setAlignment(Qt.AlignCenter)

        test_trazo = QAction("&Test del trazo", self)
        test_trazo.setStatusTip('Test del trazo que consiste en')
        test_trazo.triggered.connect(lambda: self.interfaz_trazo(self.name))
        menubar = self.menuBar()
        testMenu = menubar.addMenu('&Tests')
        testMenu.addAction(test_trazo)

        layout.addWidget(lbl1)
        self.setLayout(layout)

    def interfaz_trazo(self, name=None):
        test = Interfaz_trazo.MyWindow()
        test.show()


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    win0 = Login()          # Se establece una ventana principal
    win0.show()
    sys.exit(app.exec())
