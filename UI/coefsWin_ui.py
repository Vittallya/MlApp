# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Projects\Python\MlApp\UI\coefsWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(740, 350)
        Dialog.setMinimumSize(QtCore.QSize(740, 350))
        Dialog.setMaximumSize(QtCore.QSize(740, 350))
        Dialog.setStyleSheet("font: 9pt \"Trebuchet MS\";")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 701, 291))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame1 = QtWidgets.QFrame(self.widget)
        self.frame1.setObjectName("frame1")
        self.label = QtWidgets.QLabel(self.frame1)
        self.label.setGeometry(QtCore.QRect(1, 1, 90, 16))
        self.label.setMaximumSize(QtCore.QSize(225, 16777215))
        self.label.setObjectName("label")
        self.coefsTable = QtWidgets.QTableWidget(self.frame1)
        self.coefsTable.setGeometry(QtCore.QRect(1, 21, 701, 192))
        self.coefsTable.setObjectName("coefsTable")
        self.coefsTable.setColumnCount(0)
        self.coefsTable.setRowCount(0)
        self.verticalLayout.addWidget(self.frame1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMaximumSize(QtCore.QSize(225, 30))
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Коэффициенты и смещения"))
        self.label.setText(_translate("Dialog", "Коэффициенты:"))
        self.label_2.setText(_translate("Dialog", "Смещения"))
