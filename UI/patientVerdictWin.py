# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/patientVerdictWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(663, 416)
        Dialog.setStyleSheet("font: 9pt \"Trebuchet MS\";")
        self.bt_accept = QtWidgets.QPushButton(Dialog)
        self.bt_accept.setGeometry(QtCore.QRect(260, 360, 141, 41))
        self.bt_accept.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    font-size: 11pt;\n"
"    background-color: transparent;\n"
"    border: 2px solid rgb(38, 86, 131);\n"
"    transition: all 1s ease-out;\n"
"    color: rgb(38, 86, 131);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(38, 86, 131);\n"
"color: white;\n"
"}\n"
"")
        self.bt_accept.setObjectName("bt_accept")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(80, 90, 521, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 10, 401, 51))
        self.label.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Вердикт"))
        self.bt_accept.setText(_translate("Dialog", "Принять"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Оценка состояния пациента</span></p></body></html>"))
