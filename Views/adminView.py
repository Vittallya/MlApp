from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Services.docService import DocService
from Services.Db import Db
from UI.adminWin import Ui_MainWindow
from Services.userService import UserService
from PyQt5.QtWidgets import QMainWindow, QApplication
from Services.analyzeService import get_train_data
import pandas as pd
import numpy as np
import json
from datetime import datetime
# qt_creator_file_admin_window = "UI/docWin.ui"
# Ui_Admin_Window, QtBaseClassAdmin = uic.loadUiType(qt_creator_file_admin_window)


class AdminWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, app: QApplication, startWin:QMainWindow):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.docService = DocService(Db.unit)
        self.startWin = startWin
        self.db = Db.unit
        self.userSerivce = UserService.unit
        self.btExit.triggered.connect(self.exitAction)
        self.bt_makeAnalyze.clicked.connect(self.make_analyze_pressed)
        
        
    def make_analyze_pressed(self):
        with self.db.getConnection() as conn:
            df = pd.read_sql('''SELECT SEX, AGE13, EDUCATION, MARITAL, PROF29, EXPOSURE, ANGINA, STROKE, HYPERTENSION, COPD, TUBERCULOSIS, 	CIRRHOSIS, 	CHOLECYSTITIS, 	ULCER, 	POLYPUS, 	DIABETES, 	DEPRESSION, 	MEDICATION, 	SIGDAY, 	YEARS, 	PASSIVE, 	ALCOHOL, 	FREQ51, 	SBP1, 	DBP1, 	HEIGHT, 	WEIGHT, 	WAIST, 	THIGH, CONDITION 
        FROM "Patient_data" WHERE Condition is not NULL''', conn)

        dict_, acc = get_train_data(df)
        jsonStr = json.dumps(dict_)
        Db.unit.getFirst('''INSERT INTO "ML_DATA" (DateTime, DataJson, Accuracy) VALUES (%s, %s, %s) RETURNING Id''', (datetime.now(), jsonStr, acc))


    
    def load(self):
        self.btExit.setTitle(self.userSerivce.name)
    
    def exitAction(self):
        global window
        
        window = self.startWin
        window.show()
        self.close()        
    