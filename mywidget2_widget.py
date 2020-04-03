# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mywidget2_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MyWidget2(object):
    def setupUi(self, MyWidget2):
        MyWidget2.setObjectName("MyWidget2")
        MyWidget2.resize(175, 164)
        self.verticalLayout = QtWidgets.QVBoxLayout(MyWidget2)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(MyWidget2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.textBrowser = QtWidgets.QTextBrowser(MyWidget2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(MyWidget2)
        self.pushButton.clicked.connect(MyWidget2.button_clicked)
        QtCore.QMetaObject.connectSlotsByName(MyWidget2)

    def retranslateUi(self, MyWidget2):
        _translate = QtCore.QCoreApplication.translate
        MyWidget2.setWindowTitle(_translate("MyWidget2", "MyWidget2"))
        self.pushButton.setText(_translate("MyWidget2", "This is MyWidget2"))
