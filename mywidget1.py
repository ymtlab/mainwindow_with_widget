# -*- coding: utf-8 -*-
import sys
from mywidget1_widget import Ui_MyWidget1
from PyQt5 import QtWidgets, QtCore, QtGui

class MyWidget1(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyWidget1, self).__init__(parent)
        self.ui = Ui_MyWidget1()
        self.ui.setupUi(self)

    def button_clicked(self):
        self.find_mainwindow(self).set_text(self.ui.pushButton.text())

    def find_mainwindow(self, parent):
        if parent is None:
            return None
        if parent.inherits('QMainWindow'):
            return parent
        return self.find_mainwindow(parent.parent())
