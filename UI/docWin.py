# Form implementation generated from reading ui file 'UI/docWin.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Doc_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 555)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 771, 351))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.btMakeAnalyze = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btMakeAnalyze.setGeometry(QtCore.QRect(250, 380, 201, 51))
        self.btMakeAnalyze.setObjectName("btMakeAnalyze")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuemployeeName = QtWidgets.QMenu(parent=self.menubar)
        self.menuemployeeName.setObjectName("menuemployeeName")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exit = QtGui.QAction(parent=MainWindow)
        self.exit.setObjectName("exit")
        self.menuemployeeName.addAction(self.exit)
        self.menubar.addAction(self.menuemployeeName.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btMakeAnalyze.setText(_translate("MainWindow", "Выполнить анализ"))
        self.menuemployeeName.setTitle(_translate("MainWindow", "employeeName"))
        self.exit.setText(_translate("MainWindow", "Выход"))