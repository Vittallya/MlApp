from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QTableWidgetItem
from Services.docService import DocService
from Services.Db import Db
from Services.userService import UserService

qt_creator_file = "UI/docWin.ui"
Ui_Doc_Window, QtBaseClassDoc = uic.loadUiType(qt_creator_file)


class DocWindow(QtWidgets.QMainWindow, Ui_Doc_Window):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Doc_Window.__init__(self)
        self.setupUi(self)
        self.docService = DocService(Db.unit)
        self.btMakeAnalyze.connect(self.on_makeAnalyze_clicked)
        
    def on_makeAnalyze_clicked(self):
       pass 
        
    def load(self):
        pats = self.docService.get_doc_patients(UserService.unit.getUserGuid())
        l = len(pats)
        
        if l > 0:    
            self.tableWidget.setRowCount(l)
            self.tableWidget.setColumnCount(len(pats[0]))
            
            for row, rowValue in enumerate(pats):
                for col, colValue in enumerate(rowValue):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(colValue)))