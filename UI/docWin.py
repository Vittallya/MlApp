# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/docWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 550))
        MainWindow.setMaximumSize(QtCore.QSize(800, 550))
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("font: 9pt \"Trebuchet MS\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 781, 351))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.verticalHeader().setVisible(False)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(20, 50, 191, 19))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.editSearch = QtWidgets.QLineEdit(self.splitter)
        self.editSearch.setObjectName("editSearch")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 440, 381, 61))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btMakeAnalyze = QtWidgets.QPushButton(self.widget)
        self.btMakeAnalyze.setMinimumSize(QtCore.QSize(0, 40))
        self.btMakeAnalyze.setStyleSheet("QPushButton{\n"
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
        self.btMakeAnalyze.setObjectName("btMakeAnalyze")
        self.horizontalLayout.addWidget(self.btMakeAnalyze)
        self.btViewData = QtWidgets.QPushButton(self.widget)
        self.btViewData.setMinimumSize(QtCore.QSize(0, 40))
        self.btViewData.setStyleSheet("QPushButton{\n"
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
        self.btViewData.setObjectName("btViewData")
        self.horizontalLayout.addWidget(self.btViewData)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuemployeeName = QtWidgets.QMenu(self.menubar)
        self.menuemployeeName.setObjectName("menuemployeeName")
        MainWindow.setMenuBar(self.menubar)
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.menuemployeeName.addAction(self.exit)
        self.menubar.addAction(self.menuemployeeName.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Врач"))
        self.label.setText(_translate("MainWindow", "Поиск:"))
        self.btMakeAnalyze.setText(_translate("MainWindow", "Определить состояние"))
        self.btViewData.setText(_translate("MainWindow", "Посмотреть данные"))
        self.menuemployeeName.setTitle(_translate("MainWindow", "employeeName"))
        self.exit.setText(_translate("MainWindow", "Выход"))
