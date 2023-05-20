from UI.patientVerdictWin import Ui_Dialog
from PyQt5 import QtWidgets
from datetime import datetime

class VerdictWin(QtWidgets.QDialog, Ui_Dialog):
    
    def __init__(self, parent, data:dict) -> None:
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        
        self.bt_accept.clicked.connect(self.on_accept_clicked)
        
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(len(data.keys()) + 1)
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('ФИО пациента'))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(data.get('Fio')))
        
        self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem('Время проверки'))
        self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(str(datetime.now())))        
        
        self.tableWidget.setItem(2, 0, QtWidgets.QTableWidgetItem('Состояние пациента'))
        self.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem(data.get('state')))
        
        self.tableWidget.setItem(3, 0, QtWidgets.QTableWidgetItem('Рекомендации'))
        self.tableWidget.setItem(3, 1, QtWidgets.QTableWidgetItem(data.get('recs')))
        
        self.tableWidget.setItem(4, 0, QtWidgets.QTableWidgetItem('Оценка точности'))
        self.tableWidget.setItem(4, 1, QtWidgets.QTableWidgetItem(data.get('acc')))
        
        
    def on_accept_clicked(self):
        self.close()
        