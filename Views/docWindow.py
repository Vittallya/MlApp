from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QMainWindow, QMessageBox, QTableWidget, QTableView, QHeaderView
from Services.docService import DocService
from Services.Db import Db
from Services.userService import UserService
from Services.analyzeService import get_most_accuracy_data, is_ml_data_exists, make_analyze
from UI.docWin import Ui_MainWindow
from Services.Db import Db
import json
import pandas as pd
import numpy as np
from Views.verdictWin import VerdictWin
from Services.userService import UserService
from PyQt5.QtCore import Qt
from Views.adminView import Pat_data_nums_cols
from Views.patientDataWin import PatientDataWin
from Views.patientDataViewWin import PatientDataViewWin
#qt_creator_file = "UI/docWin.ui"
#Ui_Doc_Window, QtBaseClassDoc = uic.loadUiType(qt_creator_file)


class DocWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, app: QApplication, startWin: QMainWindow):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.app = app
        self.startWin = startWin
        self.db = Db.unit
        self.docService = DocService(Db.unit)
        self.userService = UserService.unit
        self.btMakeAnalyze.clicked.connect(self.on_makeAnalyze_clicked)
        self.exit.triggered.connect(self.exitAction)
        self.editSearch.textChanged.connect(self.on_search)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)        
        #self.tableWidget.horizontalHeader().setStretchLastSection(True) 
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.btViewData.clicked.connect(self.on_view_data_clicked)
        
        
    
    def on_view_data_clicked(self):
        rows = list(set(index.row() for index in self.tableWidget.selectedIndexes()))
            
        if len(rows) > 0:
            id = self.tableWidget.item(rows[0], 0).text() 
            
            cols = ','.join(Pat_data_nums_cols)
             
            pat_data = self.db.getFirst(f'''SELECT {cols} FROM "Patient_data"
                                            WHERE PatientId = %s''', (id,))
            if pat_data == None:
                QMessageBox(parent=self, text= "Данных для этого пациента не найдено").show()
                return
            win = PatientDataViewWin(self, pat_data)
            win.show()
            
    
    def on_search(self, text):        
        rowCount = self.tableWidget.rowCount()
        search_cols = [1,2,3]
        
        if text:                    
            
            for rowIndex in range(0, rowCount):
                self.tableWidget.hideRow(rowIndex)
            
            items = self.tableWidget.findItems(text, Qt.MatchFlag.MatchContains)
            
            for item in items:
                if item.column() in search_cols:
                    self.tableWidget.showRow(item.row())
        else:            
            for rowIndex in range(0, rowCount):
                self.tableWidget.showRow(rowIndex)
        pass
        
    
    def exitAction(self):
        global window
        
        window = self.startWin
        window.show()
        self.close()        
    
    def on_makeAnalyze_clicked(self):
        
        rows = list(set(index.row() for index in self.tableWidget.selectedIndexes()))
            
        if len(rows) > 0:
            id = self.tableWidget.item(rows[0], 0).text()     
            
            if not is_ml_data_exists(self.db):
                QMessageBox(parent=self, text= "Коэффициентов не найдено").show()
                return
                            
            cols, coefficients, bias, accuracy = get_most_accuracy_data(self.db)                          
            columns = ','.join(cols)
            
            pat_data = self.db.getFirst(f'''SELECT {columns} FROM "Patient_data"
                                            WHERE PatientId = %s''', (id,))
            if pat_data == None:
                QMessageBox(parent=self, text= "Данных для этого пациента не найдено").show()
                return
            
            number = make_analyze(pat_data, coefficients, bias)
            
            state = 'Удовлетворительное состояние'
            recs = 'Рекомендуется придерживаться ЗОЖ'
            
            match(number):
                case 1:
                    state = 'Состояние средней тяжести'
                    recs = 'Рекомендуется посетить врача'
                case 2:
                    state = 'Тяжелое состояние'
                    recs = 'Требуется немедленная госпитализация'
            
            
            surname = self.tableWidget.item(rows[0], 1).text() 
            name = self.tableWidget.item(rows[0], 2).text() 
            midname = self.tableWidget.item(rows[0], 3).text()                         
            
            initials = f'{surname} {name[0]}. {midname[0]}.'
            
            VerdictWin(self, {'acc':str(accuracy), 'state': state, 'recs':recs, 'Fio': initials}).show()
                                
        
    def load(self):
        pats = self.docService.get_doc_patients(UserService.unit.getUserGuid())
        self.menuemployeeName.setTitle(self.userService.name)
        self.tableWidget.clear()
        self.row_count = len(pats)
        
        if self.row_count > 0:    
            self.tableWidget.setRowCount(self.row_count)
            self.tableWidget.setColumnCount(len(pats[0]))
            self.tableWidget.hideColumn(0)
            self.tableWidget.setHorizontalHeaderLabels(['Ид', 'Фамилия', 'Имя', 'Отчество'])
            
            for row, rowValue in enumerate(pats):
                for col, colValue in enumerate(rowValue):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(colValue)))