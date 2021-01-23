#!/usr/bin/env python
# coding: utf-8

# In[5]:


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout,
                             QHBoxLayout, QWidget, QLabel, QFrame)
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

        for i in range(len(self.bol_ini)):
            self.tableWidget.setItem(
                i + 1, 0, QTableWidgetItem(self.bol_ini[i]))
            self.tableWidget.setItem(
                i + 1, 1, QTableWidgetItem(self.bol_fin[i]))
            self.tableWidget.setItem(
                i + 1, 2, QTableWidgetItem(self.bol_time[i]))

            if int(self.bol_ini[i]) == (int(self.bol_fin[i]) - 1):
                self.tableWidget.item(
                    i + 1, 0).setBackground(QColor(0, 255, 0))
                self.tableWidget.item(
                    i + 1, 1).setBackground(QColor(0, 255, 0))
                self.tableWidget.item(
                    i + 1, 2).setBackground(QColor(0, 255, 0))

                self.BV_act += 1

                if self.BV_act > self.BV_max:
                    self.BV_max = self.BV_act

            elif int(self.bol_ini[i]) < (int(self.bol_fin[i]) - 1):
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