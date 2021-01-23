#!/usr/bin/env python
# coding: utf-8

# In[5]:


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget,
                             QTableWidgetItem, QVBoxLayout, QHBoxLayout,
                             QWidget, QLabel, QFrame)
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt
import sys
import numpy as np
import time


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 550, 330)
        self.setWindowTitle("Resultados test")

    def initUI(self, ini, fin, tim, timv, dist):
        self.bol_ini = ini
        self.bol_fin = fin
        self.bol_time = tim
        self.bol_time_ver = timv
        self.dist = dist
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.createTable()
        self.createStat()
        self.layout = QHBoxLayout(self.centralwidget)
        self.layout.addWidget(self.tableWidget)
        self.layout.addLayout(self.statLayout)
        self.setLayout(self.layout)

    def createTable(self):
        self.BV_max = 0
        self.BV_act = 0
        self.BR_tot = 0
        self.BR_ama = 0
        self.BR_roj = 0

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(self.bol_ini) + 1)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Bolita 1"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Bolita 2"))
        self.tableWidget.setItem(0, 2, QTableWidgetItem("Tiempo"))

        orden = {'0': 0, 'A': 1, 'B': 2, 'C': 3, 'D': 4,
                 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
                 'J': 10, 'K': 11, 'L': 12, 'M': 13}

        for i in range(len(self.bol_ini)):
            self.tableWidget.setItem(
                i + 1, 0, QTableWidgetItem(self.bol_ini[i]))
            self.tableWidget.setItem(
                i + 1, 1, QTableWidgetItem(self.bol_fin[i]))
            self.tableWidget.setItem(
                i + 1, 2, QTableWidgetItem(self.bol_time[i]))

            if (int(self.bol_ini[i]) == orden.get(self.bol_fin[i]) or
                    orden.get(self.bol_ini[i]) + 1 == int(self.bol_fin[i])):
                self.tableWidget.item(
                    i + 1, 0).setBackground(QColor(0, 255, 0))
                self.tableWidget.item(
                    i + 1, 1).setBackground(QColor(0, 255, 0))
                self.tableWidget.item(
                    i + 1, 2).setBackground(QColor(0, 255, 0))

                self.BV_act += 1

                if self.BV_act > self.BV_max:
                    self.BV_max = self.BV_act

            elif (int(self.bol_ini[i]) < orden.get(self.bol_fin[i]) or
                    orden.get(self.bol_ini[i]) + 1 < int(self.bol_fin[i])):
                self.tableWidget.item(
                    i + 1, 0).setBackground(QColor(255, 0, 0))
                self.tableWidget.item(
                    i + 1, 1).setBackground(QColor(255, 0, 0))
                self.tableWidget.item(
                    i + 1, 2).setBackground(QColor(255, 0, 0))

                self.BV_act = 0
                self.BR_tot += 1
                self.BR_roj += 1

            else:
                self.tableWidget.item(
                    i + 1, 0).setBackground(QColor(255, 255, 0))
                self.tableWidget.item(
                    i + 1, 1).setBackground(QColor(255, 255, 0))
                self.tableWidget.item(
                    i + 1, 2).setBackground(QColor(255, 255, 0))

                if self.BV_act > self.BV_max:
                    self.BV_max = self.BV_act
                self.BV_act = 0
                self.BR_tot += 1
                self.BR_ama += 1

        self.tableWidget.move(0, 0)

    def createStat(self):
        self.tbx = []
        self.tbx.append(float(self.bol_time[0]))
        for i in range(len(self.bol_time) - 1):
            self.tbx.append(
                (float(self.bol_time[i + 1]) - float(self.bol_time[i])))
        self.tbx_med = round(sum(self.tbx) / (len(self.bol_time) - 1), 3)
        # x/72 pasa de pixeles a pulgadas
        self.V_med = round(
            sum([x / y for x, y in zip(self.dist, self.bol_time_ver)]) / len(self.dist), 3)
        print("distancia = ", [x for x in self.dist])
        print("tiempo = ", self.bol_time_ver)

        self.tp_ind = QLabel(str(self.bol_time[-1]))
        self.tp_ind.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.tr_ind = QLabel(str(self.bol_time[0]))
        self.tr_ind.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.tbx_ind = QLabel(str(self.tbx_med))
        self.tbx_ind.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.BV_max_ind = QLabel(str(self.BV_max))
        self.BV_max_ind.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.BR_tot_ind = QLabel(str(self.BR_tot))
        self.BR_tot_ind.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.BR_roj_ind = QLabel(str(self.BR_roj))
        self.BR_roj_ind.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.BR_ama_ind = QLabel(str(self.BR_ama))
        self.BR_ama_ind.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.V_med_ind = QLabel(str(self.V_med))
        self.V_med_ind.setFrameStyle(QFrame.Panel | QFrame.Sunken)

        self.tp_lbl = QLabel("Tiempo del proceso")
        self.tr_lbl = QLabel("Tiempo de reacción")
        self.tbx_lbl = QLabel("Tiempo de intervalo medio")
        self.BV_max_lbl = QLabel("Máximos aciertos consecutivos")
        self.BR_tot_lbl = QLabel("Número de errores totales")
        self.BR_roj_lbl = QLabel("Número de errores rojos")
        self.BR_ama_lbl = QLabel("Número de errores amarillos")
        self.V_med_lbl = QLabel("Velocidad promedio (pixel/s)")

        self.statLayout = QVBoxLayout()
        self.statLayout.addWidget(self.tp_lbl)
        self.statLayout.addWidget(self.tp_ind)
        self.statLayout.addWidget(self.tr_lbl)
        self.statLayout.addWidget(self.tr_ind)
        self.statLayout.addWidget(self.tbx_lbl)
        self.statLayout.addWidget(self.tbx_ind)
        self.statLayout.addWidget(self.BV_max_lbl)
        self.statLayout.addWidget(self.BV_max_ind)
        self.statLayout.addWidget(self.BR_tot_lbl)
        self.statLayout.addWidget(self.BR_tot_ind)
        self.statLayout.addWidget(self.BR_roj_lbl)
        self.statLayout.addWidget(self.BR_roj_ind)
        self.statLayout.addWidget(self.BR_ama_lbl)
        self.statLayout.addWidget(self.BR_ama_ind)
        self.statLayout.addWidget(self.V_med_lbl)
        self.statLayout.addWidget(self.V_med_ind)
