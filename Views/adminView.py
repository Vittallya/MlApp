from PyQt5 import QtCore, QtGui, QtWidgets, uic
from Services.docService import DocService
from Services.Db import Db
from UI.adminWin import Ui_MainWindow
from Services.userService import UserService
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox, QTableWidget
from Services.analyzeService import get_train_data
import pandas as pd
import numpy as np
import json
from datetime import datetime
from Views.patientEditWin import PatientEditWin
from Views.editEmpWin import EditEmployeeWin
from Services.employeeService import EmployeeService
from Views.coefsWin import CoefsWin
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
	"THIGH",
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
        self.bt_removeCoefs.clicked.connect(self.on_remove_clicked)
        self.bt_viewCoefs.clicked.connect(self.on_view_coefs_clicked)
        
        self.btAdd.clicked.connect(self.on_add_clicked)
        self.btRemove.clicked.connect(self.on_remove_clicked)
        self.btEdit.clicked.connect(self.on_edit_clicked)
        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.frame.hide()
        self.index = self.tabWidget.currentIndex()        
        self.empService = EmployeeService(self.db)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget_2.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)        
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)        
        self.tableAnalyze.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)        
        self.tableAnalyze.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        
   
    def on_edit_clicked(self):
        if self.index == 1:
            rows = list(set(index.row() for index in self.tableWidget_2.selectedIndexes()))
            
            if len(rows) > 0:
                id = self.tableWidget_2.item(rows[0], 0).text()
                pat_data = self.db.getFirst('''SELECT * FROM "Patient" WHERE Id = %s''', (id,))
                self.prepareWinPat(pat_data)
        elif self.index == 0:
            rows = list(set(index.row() for index in self.tableWidget.selectedIndexes()))
            
            if len(rows) > 0:
                guid = self.tableWidget.item(rows[0], 0).text()
                emp_data = self.db.getFirst('''SELECT * FROM "Employee" WHERE Guid = %s''', (guid,))
                self.prepareWinEmp(emp_data)
                
    def on_view_coefs_clicked(self):
        rows = list(set(index.row() for index in self.tableAnalyze.selectedIndexes()))
        
        if len(rows) > 0:
            rowIndex = rows[0]
            id = self.tableAnalyze.item(rowIndex, 0).text()
            
            ml_coefsDb = self.db.getFirst(''' SELECT * FROM "ML_DATA" WHERE Id = %s''', (id,))
            ml_dict = dict(json.loads(ml_coefsDb[2]))
            
            CoefsWin(self, ml_dict).show()

            
    
    def on_remove_clicked(self):
        if self.index == 1:
            rows = list(set(index.row() for index in self.tableWidget_2.selectedIndexes()))
            
            if len(rows) > 0:                
                ids = tuple(int(self.tableWidget_2.item(rowIndex, 0).text()) for rowIndex in rows)
                query = f'''DELETE FROM "Patient" WHERE Id IN ({','.join(['%s' for n in range(0, len(ids))])})'''
                self.db.execute(query, ids)
                self.reloadPatients()            
        elif self.index == 0:
            rows = list(set(index.row() for index in self.tableWidget.selectedIndexes()))
            
            if len(rows) > 0:                
                guids = tuple(self.tableWidget.item(rowIndex, 0).text() for rowIndex in rows)
                query = f'''DELETE FROM "Employee" WHERE Guid IN ({','.join(['%s' for n in range(0, len(guids))])})'''
                self.db.execute(query, guids)
                self.reload_employee_data()  
        elif self.index == 2:
            rows = list(set(index.row() for index in self.tableAnalyze.selectedIndexes()))
            
            if len(rows) > 0:                
                ids = tuple(self.tableAnalyze.item(rowIndex, 0).text() for rowIndex in rows)
                query = f'''DELETE FROM "ML_DATA" WHERE Id IN ({','.join(['%s' for n in range(0, len(ids))])})'''
                self.db.execute(query, ids)
                self.reload_analyze_data() 
            
        
    def on_add_clicked(self):
        if self.index == 1:
            self.prepareWinPat()
        else:
            self.prepareWinEmp()
            
        
    def prepareWinEmp(self, data = None):
        roles = self.db.getData('''SELECT Guid, Name from "Role" ''')
        
        self.winEmp = EditEmployeeWin(self, roles, data)
        
        self.winEmp.show()                 
        self.winEmp.pushButton.clicked.connect(self.on_emp_add_or_edit)
        
        
    def prepareWinPat(self, data = None):
        
        emps = self.db.getData('''SELECT e.Guid, e.Surname from "Employee" e
                               INNER JOIN "Role" r ON r.Guid = e.RoleGuid
                               WHERE r.Name = 'Врач' ''')
        
        self.winPat = PatientEditWin(self, emps, data)
        
        self.winPat.show()                 
        self.winPat.btAccept.clicked.connect(self.on_patient_add_or_edit)
            

    def reloadPatients(self):
        self.tableWidget_2.clear()
        pats = self.db.getData('''SELECT p.Id, p.Surname, p.Name, p.MidName, e.Surname FROM "Patient" p
                               INNER JOIN "Employee" e ON e.Guid = p.DoctorGuid''')
        l = len(pats)
        
        if l > 0:    
            self.tableWidget_2.setRowCount(l)
            self.tableWidget_2.setColumnCount(len(pats[0]))
            self.tableWidget_2.setHorizontalHeaderLabels(['Ид', 'Фамилия', 'Имя', 'Отчество', 'Лечащий врач'])
            
            for row, rowValue in enumerate(pats):
                for col, colValue in enumerate(rowValue):
                    self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(colValue)))
        
        
    def reload_analyze_data(self):
        self.tableAnalyze.clear()
        data = self.db.getData('''SELECT Id, DateTime, Accuracy FROM "ML_DATA" ''')
        l = len(data)
        
        if l > 0:    
            self.tableAnalyze.setRowCount(l)
            self.tableAnalyze.setColumnCount(len(data[0]))
            self.tableAnalyze.hideColumn(0)
            self.tableAnalyze.setHorizontalHeaderLabels(['Id','Дата и время проведения анализа', 'Оценка точности'])
            
            for row, rowValue in enumerate(data):
                for col, colValue in enumerate(rowValue):
                    self.tableAnalyze.setItem(row, col, QTableWidgetItem(str(colValue)))
        
    def reload_employee_data(self):
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
        
    def on_emp_add_or_edit(self) -> None:
        name = self.winEmp.editName.text()
        surname = self.winEmp.editSurname.text()
        midname = self.winEmp.editMidname.text()
        roleGuid = self.winEmp.cmRoles.currentData()
        login = self.winEmp.editLogin.text()
        password = self.winEmp.editPassword.text()
        password_else = self.winEmp.editPassword_2.text()
        guid = self.winEmp.empGuid
        prevLogin = self.winEmp.prevLogin
        psw_empty = len(self.winEmp.editPassword.text()) == 0 and len(self.winEmp.editPassword_2.text()) == 0
        
        
        
        if not self.winEmp.isEdit or self.winEmp.cbChangeLoginPsw.isChecked():                    
            if  password != password_else:
                QMessageBox(parent= self, text="Пароли не совпадают").show()
                return
            
            if  (self.winEmp.isEdit or prevLogin != login) and self.empService.is_login_exists(login):
                QMessageBox(parent= self, text="Такой логин уже существует. Введите уникальный логин").show()
                return
        elif self.winEmp.isEdit:
            self.empService.update_emp_without_usr_data(guid, name, surname, midname, roleGuid)
            return
        
        
        self.empService.add_or_edit_employee(guid, name, surname, midname, login, password, roleGuid)
        self.winEmp.close()
        self.reload_employee_data()
        
        
    def on_patient_add_or_edit(self) -> None:
        
        name = self.winPat.editName.text()
        surname = self.winPat.editLastName.text()
        midname = self.winPat.editMidName.text()
        doctorGuid = self.winPat.cmDoctors.currentData()
        id = None
        
        if self.winPat.isEdit:
            id = self.winPat.patData[0]
            self.db.execute('''UPDATE "Patient" SET Name = %s, Surname = %s, Midname = %s, DoctorGuid = %s
                            WHERE Id = %s''',
                            (name, surname, midname, doctorGuid, id))            
        else:        
            id = self.db.getFirst('''INSERT INTO "Patient"(Name, Surname, Midname, DoctorGuid) VALUES
                        (%s, %s, %s, %s) RETURNING Id''', (name, surname, midname, doctorGuid))[0]
        
        if self.winPat.patDataNums != None:
        
            patNums = self.winPat.patDataNums
            
            if self.winPat.patDataNumsAlreadyExists:
                query = f'''UPDATE "Patient_data" SET {", ".join([col + ' = %s' for col in Pat_data_nums_cols])}
                            WHERE Id = %s'''
                                        
                params = [str(p) for p in patNums]
                params.append(str(self.winPat.patNumsId))
                
                self.db.execute(query, tuple(params))
                
            else:            
                colStr = ','.join(Pat_data_nums_cols)
                valuesStr = ','.join(['%s' for i in range(0, len(patNums) + 1)])
                
                params = (str(id),) + tuple(str(p) for p in patNums)
                query = f'''INSERT INTO "Patient_data"(PatientId, {colStr}) VALUES ({valuesStr})'''                
                self.db.execute(query,params)
        
        self.winPat.close()
        self.reloadPatients()
        pass    
    
    def tab_changed(self):
        self.index = self.tabWidget.currentIndex()
        if self.index == 2:
            self.frame.hide()
            self.frame1.show()
        else:
            self.frame.show()
            self.frame1.hide()
    
    def make_analyze_pressed(self):
        with self.db.getConnection() as conn:
            df = pd.read_sql('''SELECT SEX, AGE13, EDUCATION, MARITAL, PROF29, EXPOSURE, ANGINA, STROKE, HYPERTENSION, COPD, TUBERCULOSIS, 	CIRRHOSIS, 	CHOLECYSTITIS, 	ULCER, 	POLYPUS, 	DIABETES, 	DEPRESSION, 	MEDICATION, 	SIGDAY, 	YEARS, 	PASSIVE, 	ALCOHOL, 	FREQ51, 	SBP1, 	DBP1, 	HEIGHT, 	WEIGHT, 	WAIST, 	THIGH, CONDITION 
        FROM "Patient_data" WHERE Condition is not NULL''', conn)

        dict_, acc = get_train_data(df)
        jsonStr = json.dumps(dict_)
        Db.unit.getFirst('''INSERT INTO "ML_DATA" (DateTime, DataJson, Accuracy) VALUES (%s, %s, %s) RETURNING Id''', (datetime.now(), jsonStr, acc))
        self.reload_analyze_data()                
    
    def load(self):
        self.btExit.setTitle(self.userSerivce.name)
        self.reloadPatients()
        self.reload_employee_data()
        self.reload_analyze_data()
        
    def exitAction(self):
        global window
        
        window = self.startWin
        window.show()
        self.close()        
    