from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QMainWindow
from Services.docService import DocService
from Services.Db import Db
from Services.userService import UserService
from Services.analyzeService import make_analyze
from UI.docWin import Ui_MainWindow
from Services.Db import Db
import json
import pandas as pd
import numpy as np
from Views.verdictWin import VerdictWin
from Services.userService import UserService

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
    
    def exitAction(self):
        global window
        
        window = self.startWin
        window.show()
        self.close()        
    
    def on_makeAnalyze_clicked(self):
        
        items = self.tableWidget.selectedItems()
        
        if len(items) == 5:
            id = items[0].text()
            ml_data_db = self.db.getFirst('''SELECT DataJson, Accuracy FROM "ML_DATA" ORDER BY Accuracy DESC LIMIT 1''')
            
            if ml_data_db != None:   
                accuracy = float(ml_data_db[1])
                data_ml = dict(json.loads(ml_data_db[0]))                
                cols = data_ml.get('columns')                
                columns = ','.join(cols)
                
                pat_data = self.db.getFirst(f'''SELECT {columns} FROM "Patient_data"
                                                WHERE PatientId = %s''', (id,))
                if pat_data != None:
                    coefficients = pd.DataFrame(data_ml["coefficients"])    
                    bias = np.array(data_ml["bias"])
                    number = make_analyze(pat_data, coefficients, bias)
                    
                    state = 'Удовлетворительное состояние'
                    recs = 'Рекомендуется придерживаться ЗОЖ'
                    
                    match(number):
                        case [1]:
                            state = 'Состояние средней тяжести'
                            recs = 'Рекомендуется посетить врача'
                        case [2]:
                            state = 'Тяжелое состояние'
                            recs = 'Требуется немедленная госпитализация'
                    
                    VerdictWin(state, recs, accuracy, self).show()
                                
        
    def load(self):
        pats = self.docService.get_doc_patients(UserService.unit.getUserGuid())
        self.menuemployeeName.setTitle(self.userService.name)
        self.tableWidget.clear()
        l = len(pats)
        
        if l > 0:    
            self.tableWidget.setRowCount(l)
            self.tableWidget.setColumnCount(len(pats[0]))
            
            for row, rowValue in enumerate(pats):
                for col, colValue in enumerate(rowValue):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(colValue)))