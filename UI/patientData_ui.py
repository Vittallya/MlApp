# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Projects\Python\MlApp\UI\patientData.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 290)
        Dialog.setMinimumSize(QtCore.QSize(1000, 290))
        Dialog.setMaximumSize(QtCore.QSize(1000, 290))
        Dialog.setStyleSheet("font: 10pt \"Trebuchet MS\";")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 210, 141, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 10, 921, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setMinimum(1.0)
        self.doubleSpinBox.setMaximum(2.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.verticalLayout.addWidget(self.doubleSpinBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_2.setDecimals(0)
        self.doubleSpinBox_2.setMinimum(0.0)
        self.doubleSpinBox_2.setMaximum(150.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.verticalLayout_2.addWidget(self.doubleSpinBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_3.setDecimals(0)
        self.doubleSpinBox_3.setMinimum(0.0)
        self.doubleSpinBox_3.setMaximum(4.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.verticalLayout_3.addWidget(self.doubleSpinBox_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_4.setDecimals(0)
        self.doubleSpinBox_4.setMinimum(0.0)
        self.doubleSpinBox_4.setMaximum(3.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.verticalLayout_4.addWidget(self.doubleSpinBox_4)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_5.setDecimals(0)
        self.doubleSpinBox_5.setMinimum(1.0)
        self.doubleSpinBox_5.setMaximum(7.0)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.verticalLayout_5.addWidget(self.doubleSpinBox_5)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_7.setDecimals(0)
        self.doubleSpinBox_7.setMinimum(1.0)
        self.doubleSpinBox_7.setMaximum(7.0)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.verticalLayout_7.addWidget(self.doubleSpinBox_7)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_8.setDecimals(0)
        self.doubleSpinBox_8.setMinimum(0.0)
        self.doubleSpinBox_8.setMaximum(1.0)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.verticalLayout_8.addWidget(self.doubleSpinBox_8)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_9.setDecimals(0)
        self.doubleSpinBox_9.setMinimum(0.0)
        self.doubleSpinBox_9.setMaximum(1.0)
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.verticalLayout_9.addWidget(self.doubleSpinBox_9)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_10.setDecimals(0)
        self.doubleSpinBox_10.setMinimum(0.0)
        self.doubleSpinBox_10.setMaximum(1.0)
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.verticalLayout_10.addWidget(self.doubleSpinBox_10)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_6.setDecimals(0)
        self.doubleSpinBox_6.setMinimum(0.0)
        self.doubleSpinBox_6.setMaximum(1.0)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.verticalLayout_6.addWidget(self.doubleSpinBox_6)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_30.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_11.addWidget(self.label_11)
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_11.setDecimals(0)
        self.doubleSpinBox_11.setMinimum(0.0)
        self.doubleSpinBox_11.setMaximum(1.0)
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.verticalLayout_11.addWidget(self.doubleSpinBox_11)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_12.addWidget(self.label_12)
        self.doubleSpinBox_12 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_12.setDecimals(0)
        self.doubleSpinBox_12.setMinimum(0.0)
        self.doubleSpinBox_12.setMaximum(1.0)
        self.doubleSpinBox_12.setObjectName("doubleSpinBox_12")
        self.verticalLayout_12.addWidget(self.doubleSpinBox_12)
        self.horizontalLayout_2.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_13.addWidget(self.label_13)
        self.doubleSpinBox_13 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_13.setDecimals(0)
        self.doubleSpinBox_13.setMinimum(0.0)
        self.doubleSpinBox_13.setMaximum(1.0)
        self.doubleSpinBox_13.setObjectName("doubleSpinBox_13")
        self.verticalLayout_13.addWidget(self.doubleSpinBox_13)
        self.horizontalLayout_2.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_14.addWidget(self.label_14)
        self.doubleSpinBox_14 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_14.setDecimals(0)
        self.doubleSpinBox_14.setMinimum(0.0)
        self.doubleSpinBox_14.setMaximum(1.0)
        self.doubleSpinBox_14.setObjectName("doubleSpinBox_14")
        self.verticalLayout_14.addWidget(self.doubleSpinBox_14)
        self.horizontalLayout_2.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_15.addWidget(self.label_15)
        self.doubleSpinBox_15 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_15.setDecimals(0)
        self.doubleSpinBox_15.setMinimum(0.0)
        self.doubleSpinBox_15.setMaximum(1.0)
        self.doubleSpinBox_15.setObjectName("doubleSpinBox_15")
        self.verticalLayout_15.addWidget(self.doubleSpinBox_15)
        self.horizontalLayout_2.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_16.addWidget(self.label_16)
        self.doubleSpinBox_16 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_16.setDecimals(0)
        self.doubleSpinBox_16.setMinimum(0.0)
        self.doubleSpinBox_16.setMaximum(1.0)
        self.doubleSpinBox_16.setObjectName("doubleSpinBox_16")
        self.verticalLayout_16.addWidget(self.doubleSpinBox_16)
        self.horizontalLayout_2.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_17.addWidget(self.label_17)
        self.doubleSpinBox_17 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_17.setDecimals(0)
        self.doubleSpinBox_17.setMinimum(0.0)
        self.doubleSpinBox_17.setMaximum(1.0)
        self.doubleSpinBox_17.setObjectName("doubleSpinBox_17")
        self.verticalLayout_17.addWidget(self.doubleSpinBox_17)
        self.horizontalLayout_2.addLayout(self.verticalLayout_17)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_18.addWidget(self.label_18)
        self.doubleSpinBox_18 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_18.setDecimals(0)
        self.doubleSpinBox_18.setMinimum(0.0)
        self.doubleSpinBox_18.setMaximum(1.0)
        self.doubleSpinBox_18.setObjectName("doubleSpinBox_18")
        self.verticalLayout_18.addWidget(self.doubleSpinBox_18)
        self.horizontalLayout_2.addLayout(self.verticalLayout_18)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_19.addWidget(self.label_19)
        self.doubleSpinBox_19 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_19.setDecimals(0)
        self.doubleSpinBox_19.setMinimum(0.0)
        self.doubleSpinBox_19.setMaximum(1000.0)
        self.doubleSpinBox_19.setObjectName("doubleSpinBox_19")
        self.verticalLayout_19.addWidget(self.doubleSpinBox_19)
        self.horizontalLayout_2.addLayout(self.verticalLayout_19)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_20.addWidget(self.label_20)
        self.doubleSpinBox_20 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_20.setDecimals(0)
        self.doubleSpinBox_20.setMinimum(0.0)
        self.doubleSpinBox_20.setMaximum(150.0)
        self.doubleSpinBox_20.setObjectName("doubleSpinBox_20")
        self.verticalLayout_20.addWidget(self.doubleSpinBox_20)
        self.horizontalLayout_2.addLayout(self.verticalLayout_20)
        self.verticalLayout_30.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_21.addWidget(self.label_21)
        self.doubleSpinBox_21 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_21.setDecimals(0)
        self.doubleSpinBox_21.setMinimum(0.0)
        self.doubleSpinBox_21.setMaximum(1.0)
        self.doubleSpinBox_21.setObjectName("doubleSpinBox_21")
        self.verticalLayout_21.addWidget(self.doubleSpinBox_21)
        self.horizontalLayout_3.addLayout(self.verticalLayout_21)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_22.addWidget(self.label_22)
        self.doubleSpinBox_22 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_22.setDecimals(0)
        self.doubleSpinBox_22.setMinimum(0.0)
        self.doubleSpinBox_22.setMaximum(1.0)
        self.doubleSpinBox_22.setObjectName("doubleSpinBox_22")
        self.verticalLayout_22.addWidget(self.doubleSpinBox_22)
        self.horizontalLayout_3.addLayout(self.verticalLayout_22)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_23.addWidget(self.label_23)
        self.doubleSpinBox_23 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_23.setDecimals(0)
        self.doubleSpinBox_23.setMinimum(0.0)
        self.doubleSpinBox_23.setMaximum(7.0)
        self.doubleSpinBox_23.setObjectName("doubleSpinBox_23")
        self.verticalLayout_23.addWidget(self.doubleSpinBox_23)
        self.horizontalLayout_3.addLayout(self.verticalLayout_23)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_24 = QtWidgets.QLabel(self.layoutWidget)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_24.addWidget(self.label_24)
        self.doubleSpinBox_24 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_24.setDecimals(0)
        self.doubleSpinBox_24.setMinimum(0.0)
        self.doubleSpinBox_24.setMaximum(200.0)
        self.doubleSpinBox_24.setObjectName("doubleSpinBox_24")
        self.verticalLayout_24.addWidget(self.doubleSpinBox_24)
        self.horizontalLayout_3.addLayout(self.verticalLayout_24)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_25 = QtWidgets.QLabel(self.layoutWidget)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_25.addWidget(self.label_25)
        self.doubleSpinBox_25 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_25.setDecimals(0)
        self.doubleSpinBox_25.setMinimum(0.0)
        self.doubleSpinBox_25.setMaximum(200.0)
        self.doubleSpinBox_25.setObjectName("doubleSpinBox_25")
        self.verticalLayout_25.addWidget(self.doubleSpinBox_25)
        self.horizontalLayout_3.addLayout(self.verticalLayout_25)
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_26 = QtWidgets.QLabel(self.layoutWidget)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_26.addWidget(self.label_26)
        self.doubleSpinBox_26 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_26.setDecimals(0)
        self.doubleSpinBox_26.setMinimum(1.0)
        self.doubleSpinBox_26.setMaximum(250.0)
        self.doubleSpinBox_26.setObjectName("doubleSpinBox_26")
        self.verticalLayout_26.addWidget(self.doubleSpinBox_26)
        self.horizontalLayout_3.addLayout(self.verticalLayout_26)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_27.addWidget(self.label_27)
        self.doubleSpinBox_27 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_27.setDecimals(0)
        self.doubleSpinBox_27.setMinimum(0.0)
        self.doubleSpinBox_27.setMaximum(300.0)
        self.doubleSpinBox_27.setObjectName("doubleSpinBox_27")
        self.verticalLayout_27.addWidget(self.doubleSpinBox_27)
        self.horizontalLayout_3.addLayout(self.verticalLayout_27)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_28.addWidget(self.label_28)
        self.doubleSpinBox_28 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_28.setDecimals(0)
        self.doubleSpinBox_28.setMinimum(0.0)
        self.doubleSpinBox_28.setMaximum(200.0)
        self.doubleSpinBox_28.setObjectName("doubleSpinBox_28")
        self.verticalLayout_28.addWidget(self.doubleSpinBox_28)
        self.horizontalLayout_3.addLayout(self.verticalLayout_28)
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.label_29 = QtWidgets.QLabel(self.layoutWidget)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_29.addWidget(self.label_29)
        self.doubleSpinBox_29 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_29.setDecimals(0)
        self.doubleSpinBox_29.setMinimum(0.0)
        self.doubleSpinBox_29.setMaximum(200.0)
        self.doubleSpinBox_29.setObjectName("doubleSpinBox_29")
        self.verticalLayout_29.addWidget(self.doubleSpinBox_29)
        self.horizontalLayout_3.addLayout(self.verticalLayout_29)
        self.verticalLayout_30.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Применить"))
        self.label.setText(_translate("Dialog", "Пол"))
        self.label_2.setText(_translate("Dialog", "Возраст"))
        self.label_3.setText(_translate("Dialog", "Образование"))
        self.label_4.setText(_translate("Dialog", "Сем. полож."))
        self.label_5.setText(_translate("Dialog", "Спец-ция"))
        self.label_7.setText(_translate("Dialog", "Вр. усл. труда"))
        self.label_8.setText(_translate("Dialog", "Стенокардия"))
        self.label_9.setText(_translate("Dialog", "Инсульт"))
        self.label_10.setText(_translate("Dialog", "Гипертония"))
        self.label_6.setText(_translate("Dialog", "ХОБЛ"))
        self.label_11.setText(_translate("Dialog", "Туберкулез"))
        self.label_12.setText(_translate("Dialog", "Цирроз"))
        self.label_13.setText(_translate("Dialog", "Холецистит"))
        self.label_14.setText(_translate("Dialog", "Язва"))
        self.label_15.setText(_translate("Dialog", "Полип"))
        self.label_16.setText(_translate("Dialog", "Диабет"))
        self.label_17.setText(_translate("Dialog", "Депрессия"))
        self.label_18.setText(_translate("Dialog", "Медикаменты"))
        self.label_19.setText(_translate("Dialog", "Сиг/день"))
        self.label_20.setText(_translate("Dialog", "Стаж курения"))
        self.label_21.setText(_translate("Dialog", "Пассивное кур-е"))
        self.label_22.setText(_translate("Dialog", "Алкоголь"))
        self.label_23.setText(_translate("Dialog", "Алк. дн/нед"))
        self.label_24.setText(_translate("Dialog", "Сист. давление"))
        self.label_25.setText(_translate("Dialog", "Диаст. давление"))
        self.label_26.setText(_translate("Dialog", "Рост"))
        self.label_27.setText(_translate("Dialog", "Вес"))
        self.label_28.setText(_translate("Dialog", "Талия"))
        self.label_29.setText(_translate("Dialog", "Объем бедер"))
