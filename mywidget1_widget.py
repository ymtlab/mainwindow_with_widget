# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mywidget1_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MyWidget1(object):
    def setupUi(self, MyWidget1):
        MyWidget1.setObjectName("MyWidget1")
        MyWidget1.resize(168, 165)
        self.verticalLayout = QtWidgets.QVBoxLayout(MyWidget1)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(MyWidget1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.textBrowser = QtWidgets.QTextBrowser(MyWidget1)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(MyWidget1)
        self.pushButton.clicked.connect(MyWidget1.button_clicked)
        QtCore.QMetaObject.connectSlotsByName(MyWidget1)

    def retranslateUi(self, MyWidget1):
        _translate = QtCore.QCoreApplication.translate
        MyWidget1.setWindowTitle(_translate("MyWidget1", "MyWidget1"))
        self.pushButton.setText(_translate("MyWidget1", "This is MyWidget1"))
