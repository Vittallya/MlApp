# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Projects\Python\MlApp\UI\patientEditWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(511, 690)
        Dialog.setStyleSheet("font-size: 12pt;")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(170, 600, 161, 51))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(130, 20, 439, 51))
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 100, 451, 411))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.editLastName = QtWidgets.QLineEdit(self.widget)
        self.editLastName.setText("")
        self.editLastName.setObjectName("editLastName")
        self.verticalLayout.addWidget(self.editLastName)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.editName = QtWidgets.QLineEdit(self.widget)
        self.editName.setText("")
        self.editName.setObjectName("editName")
        self.verticalLayout.addWidget(self.editName)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.editMidName = QtWidgets.QLineEdit(self.widget)
        self.editMidName.setText("")
        self.editMidName.setObjectName("editMidName")
        self.verticalLayout.addWidget(self.editMidName)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.cmDoctors = QtWidgets.QComboBox(self.widget)
        self.cmDoctors.setObjectName("cmDoctors")
        self.verticalLayout.addWidget(self.cmDoctors)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setStyleSheet("margin-top: 10px;\n"
"")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Применить"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Добавить новую запись</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "Фамилия"))
        self.label_2.setText(_translate("Dialog", "Имя"))
        self.label_3.setText(_translate("Dialog", "Отчество"))
        self.label_4.setText(_translate("Dialog", "Доктор"))
        self.pushButton_2.setText(_translate("Dialog", "Данные..."))
