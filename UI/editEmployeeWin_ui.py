# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Projects\Python\MlApp\UI\editEmployeeWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(544, 727)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 650, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(100, 10, 341, 51))
        self.label_8.setStyleSheet("font-size: 16pt;\n"
"font-weight: bold;\n"
"")
        self.label_8.setObjectName("label_8")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 100, 481, 521))
        self.widget.setObjectName("widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.editSurname = QtWidgets.QLineEdit(self.widget)
        self.editSurname.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.editSurname.setObjectName("editSurname")
        self.verticalLayout.addWidget(self.editSurname)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.editName = QtWidgets.QLineEdit(self.widget)
        self.editName.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.editName.setObjectName("editName")
        self.verticalLayout_2.addWidget(self.editName)
        self.verticalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.editMidname = QtWidgets.QLineEdit(self.widget)
        self.editMidname.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.editMidname.setObjectName("editMidname")
        self.verticalLayout_3.addWidget(self.editMidname)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.cmRoles = QtWidgets.QComboBox(self.widget)
        self.cmRoles.setObjectName("cmRoles")
        self.verticalLayout_6.addWidget(self.cmRoles)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.cbChangeLoginPsw = QtWidgets.QCheckBox(self.widget)
        self.cbChangeLoginPsw.setObjectName("cbChangeLoginPsw")
        self.verticalLayout_8.addWidget(self.cbChangeLoginPsw)
        self.boxLogin = QtWidgets.QVBoxLayout()
        self.boxLogin.setObjectName("boxLogin")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.boxLogin.addWidget(self.label_4)
        self.editLogin = QtWidgets.QLineEdit(self.widget)
        self.editLogin.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.editLogin.setObjectName("editLogin")
        self.boxLogin.addWidget(self.editLogin)
        self.verticalLayout_8.addLayout(self.boxLogin)
        self.boxPsw = QtWidgets.QVBoxLayout()
        self.boxPsw.setObjectName("boxPsw")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.boxPsw.addWidget(self.label_5)
        self.editPassword = QtWidgets.QLineEdit(self.widget)
        self.editPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.editPassword.setObjectName("editPassword")
        self.boxPsw.addWidget(self.editPassword)
        self.verticalLayout_8.addLayout(self.boxPsw)
        self.boxPswElse = QtWidgets.QVBoxLayout()
        self.boxPswElse.setObjectName("boxPswElse")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.boxPswElse.addWidget(self.label_7)
        self.editPassword_2 = QtWidgets.QLineEdit(self.widget)
        self.editPassword_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.editPassword_2.setObjectName("editPassword_2")
        self.boxPswElse.addWidget(self.editPassword_2)
        self.verticalLayout_8.addLayout(self.boxPswElse)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Применить"))
        self.label_8.setWhatsThis(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Добавить нового сотрудника</p></body></html>"))
        self.label.setText(_translate("Dialog", "Фамилия"))
        self.label_2.setText(_translate("Dialog", "Имя"))
        self.label_3.setText(_translate("Dialog", "Отчество"))
        self.label_6.setText(_translate("Dialog", "Роль"))
        self.cbChangeLoginPsw.setText(_translate("Dialog", "Изменить логин и (-или) пароль"))
        self.label_4.setText(_translate("Dialog", "Логин в системе"))
        self.label_5.setText(_translate("Dialog", "Пароль"))
        self.label_7.setText(_translate("Dialog", "Пароль еще раз"))
