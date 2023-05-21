# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Projects\Python\MlApp\UI\adminWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 520)
        MainWindow.setMinimumSize(QtCore.QSize(800, 520))
        MainWindow.setMaximumSize(QtCore.QSize(800, 520))
        MainWindow.setStyleSheet("font: 10pt \"Trebuchet MS\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 771, 311))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 741, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 10, 741, 251))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableAnalyze = QtWidgets.QTableWidget(self.tab_3)
        self.tableAnalyze.setGeometry(QtCore.QRect(10, 10, 741, 251))
        self.tableAnalyze.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableAnalyze.setShowGrid(True)
        self.tableAnalyze.setRowCount(0)
        self.tableAnalyze.setColumnCount(0)
        self.tableAnalyze.setObjectName("tableAnalyze")
        self.tableAnalyze.horizontalHeader().setVisible(True)
        self.tableAnalyze.horizontalHeader().setCascadingSectionResizes(True)
        self.tableAnalyze.horizontalHeader().setSortIndicatorShown(False)
        self.tableAnalyze.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_3, "")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 360, 643, 104))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btAdd = QtWidgets.QPushButton(self.frame)
        self.btAdd.setMinimumSize(QtCore.QSize(0, 30))
        self.btAdd.setObjectName("btAdd")
        self.horizontalLayout.addWidget(self.btAdd)
        self.btEdit = QtWidgets.QPushButton(self.frame)
        self.btEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.btEdit.setObjectName("btEdit")
        self.horizontalLayout.addWidget(self.btEdit)
        self.btRemove = QtWidgets.QPushButton(self.frame)
        self.btRemove.setMinimumSize(QtCore.QSize(0, 30))
        self.btRemove.setObjectName("btRemove")
        self.horizontalLayout.addWidget(self.btRemove)
        self.verticalLayout.addWidget(self.frame)
        self.frame1 = QtWidgets.QFrame(self.layoutWidget)
        self.frame1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame1.setObjectName("frame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame1)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_viewCoefs = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_viewCoefs.sizePolicy().hasHeightForWidth())
        self.bt_viewCoefs.setSizePolicy(sizePolicy)
        self.bt_viewCoefs.setMinimumSize(QtCore.QSize(220, 30))
        self.bt_viewCoefs.setObjectName("bt_viewCoefs")
        self.horizontalLayout_2.addWidget(self.bt_viewCoefs)
        self.bt_makeAnalyze = QtWidgets.QPushButton(self.frame1)
        self.bt_makeAnalyze.setMinimumSize(QtCore.QSize(280, 30))
        self.bt_makeAnalyze.setObjectName("bt_makeAnalyze")
        self.horizontalLayout_2.addWidget(self.bt_makeAnalyze)
        self.bt_removeCoefs = QtWidgets.QPushButton(self.frame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_removeCoefs.sizePolicy().hasHeightForWidth())
        self.bt_removeCoefs.setSizePolicy(sizePolicy)
        self.bt_removeCoefs.setMinimumSize(QtCore.QSize(100, 30))
        self.bt_removeCoefs.setObjectName("bt_removeCoefs")
        self.horizontalLayout_2.addWidget(self.bt_removeCoefs)
        self.verticalLayout.addWidget(self.frame1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.btExit = QtWidgets.QMenu(self.menubar)
        self.btExit.setObjectName("btExit")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.btExit.addAction(self.action)
        self.menubar.addAction(self.btExit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Сотрудники"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Пациенты"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Анализ"))
        self.btAdd.setText(_translate("MainWindow", "Добавить"))
        self.btEdit.setText(_translate("MainWindow", "Редактировать"))
        self.btRemove.setText(_translate("MainWindow", "Удалить"))
        self.bt_viewCoefs.setText(_translate("MainWindow", "Посмотреть коэффициенты"))
        self.bt_makeAnalyze.setText(_translate("MainWindow", "Получить новые коэффициенты"))
        self.bt_removeCoefs.setText(_translate("MainWindow", "Удалить"))
        self.btExit.setTitle(_translate("MainWindow", "name"))
        self.action.setText(_translate("MainWindow", "Выйти"))
