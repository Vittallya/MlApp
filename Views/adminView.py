from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Services.docService import DocService
from Services.Db import Db
from UI.adminWin import Ui_MainWindow
from Services.userService import UserService
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from Services.analyzeService import get_train_data
import pandas as pd
import numpy as np
import json
from datetime import datetime
from Views.patientEditWin import PatientEditWin
# qt_creator_file_admin_window = "UI/docWin.ui"
# Ui_Admin_Window, QtBaseClassAdmin = uic.loadUiType(qt_creator_file_admin_window)


Pat_data_nums_cols = [
    "SEX",
	"AGE13",
	"EDUCATION",
	"MARITAL",
	"PROF29",
	"EXPOSURE",
	"ANGINA",
	"STROKE",
	"HYPERTENSION",
	"COPD",
	"TUBERCULOSIS",
	"CIRRHOSIS",
	"CHOLECYSTITIS",
	"ULCER",
	"POLYPUS",
	"DIABETES",
	"DEPRESSION",
	"MEDICATION",
	"SIGDAY",
	"YEARS",
	"PASSIVE",
	"ALCOHOL",
	"FREQ51",
	"SBP1",
	"DBP1",
	"HEIGHT",
	"WEIGHT",
	"WAIST",
]


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
        self.btAdd.clicked.connect(self.on_add_clicked)
        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.frame.hide()
        self.index = self.tabWidget.currentIndex()        
        
    
    def on_add_clicked(self):
        if self.index == 1:
            self.prepareWinPat()
            
        
    def prepareWinPat(self, data = None):
        self.winPat = PatientEditWin(self, data)
        
        self.winPat.show()
        emps = self.db.getData('''SELECT e.Guid, e.Surname from "Employee" e
                               INNER JOIN "Role" r ON r.Guid = e.RoleGuid
                               WHERE r.Name = 'Врач' ''')
        self.winPat.cmDoctors.clear()
        
        for emp in emps:
            self.winPat.cmDoctors.addItem(str(emp[1]), emp[0])        
        
        if data == None:
            self.winPat.btAccept.clicked.connect(self.on_patient_add)

    def reloadPatients(self):
        self.tableWidget_2.clear()
        pats = self.db.getData('''SELECT p.Surname, p.Name, p.MidName, e.Surname FROM "Patient" p
                               INNER JOIN "Employee" e ON e.Guid = p.DoctorGuid''')
        l = len(pats)
        
        if l > 0:    
            self.tableWidget_2.setRowCount(l)
            self.tableWidget_2.setColumnCount(len(pats[0]))
            self.tableWidget_2.setHorizontalHeaderLabels(['Фамилия', 'Имя', 'Отчество', 'Лечащий врач'])
            
            for row, rowValue in enumerate(pats):
                for col, colValue in enumerate(rowValue):
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(colValue)))
        
        
    def reloadEmployees(self):
        self.tableWidget.clear()
        emps = self.db.getData('''SELECT e.Guid, e.Surname, e.Name, e.Midname, r.Name FROM "Employee" e 
                               INNER JOIN "Role" r ON r.Guid = e.RoleGuid''')
        l = len(emps)
        
        if l > 0:    
            self.tableWidget.setRowCount(l)
            self.tableWidget.setColumnCount(len(emps[0]))
            self.tableWidget.setHorizontalHeaderLabels(['UID', 'Фамилия', 'Имя', 'Отчество', 'Роль в системе'])
            
            for row, rowValue in enumerate(emps):
                for col, colValue in enumerate(rowValue):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(colValue)))
        
    def on_patient_add(self) -> None:
        name = self.winPat.editName.text()
        surname = self.winPat.editLastName.text()
        midname = self.winPat.editMidName.text()
        doctorGuid = self.winPat.cmDoctors.currentData()
        
        id = self.db.getFirst('''INSERT INTO "Patient"(Name, Surname, Midname, DoctorGuid) VALUES
                        (%s, %s, %s, %s) RETURNING Id''', (name, surname, midname, doctorGuid))
        
        #цифры для пациента здесь еще не могут существовать, поэтому они добавляются
        if self.winPat.patDataNums != None:
        
        
            # окне где-то лишний элемент
            patDataNums = self.winPat.patDataNums
            
            colStr = ','.join(Pat_data_nums_cols)
            valuesStr = ','.join([str(num) for num in patDataNums])
            
            self.db.execute(f'''INSERT INTO "Patient_data"(PatientId, {colStr}) VALUES (%s, {valuesStr}) ''',
                            (id[0],))
        
        self.winPat.close()
        self.reloadPatients()
        pass    
    
    def tab_changed(self):
        self.index = self.tabWidget.currentIndex()
        if self.index == 2:
            self.frame.hide()
        else:
            self.frame.show()
    
    def make_analyze_pressed(self):
        with self.db.getConnection() as conn:
            df = pd.read_sql('''SELECT SEX, AGE13, EDUCATION, MARITAL, PROF29, EXPOSURE, ANGINA, STROKE, HYPERTENSION, COPD, TUBERCULOSIS, 	CIRRHOSIS, 	CHOLECYSTITIS, 	ULCER, 	POLYPUS, 	DIABETES, 	DEPRESSION, 	MEDICATION, 	SIGDAY, 	YEARS, 	PASSIVE, 	ALCOHOL, 	FREQ51, 	SBP1, 	DBP1, 	HEIGHT, 	WEIGHT, 	WAIST, 	THIGH, CONDITION 
        FROM "Patient_data" WHERE Condition is not NULL''', conn)

        dict_, acc = get_train_data(df)
        jsonStr = json.dumps(dict_)
        Db.unit.getFirst('''INSERT INTO "ML_DATA" (DateTime, DataJson, Accuracy) VALUES (%s, %s, %s) RETURNING Id''', (datetime.now(), jsonStr, acc))


    
    def load(self):
        self.btExit.setTitle(self.userSerivce.name)
        self.reloadPatients()
        self.reloadEmployees()
    
    def exitAction(self):
        global window
        
        window = self.startWin
        window.show()
        self.close()        
    