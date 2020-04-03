# -*- coding: utf-8 -*-
import sys
from mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def button_clicked(self):
        self.set_text(self.ui.pushButton.text())

    def set_text(self, text):
        self.ui.textBrowser.setText(text)
        childTextBrowser = self.ui.dockWidget.findChild(QtWidgets.QTextBrowser)
        childTextBrowser.setText(text)
        childTextBrowser = self.ui.dockWidget_2.findChild(QtWidgets.QTextBrowser)
        childTextBrowser.setText(text)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
 
if __name__ == '__main__':
    main()
