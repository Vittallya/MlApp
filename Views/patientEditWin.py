from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QMainWindow, QDialog, QComboBox, QDoubleSpinBox
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
from UI.patientEditWin import Ui_Dialog
from Views.patientDataWin import PatientDataWin
from Services.Db import Db

class PatientEditWin(QDialog, Ui_Dialog):
    
    def __init__(self, parent, patData = None) -> None:
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.isEdit = patData != None
        self.patData = patData
        self.btSwitchToData.clicked.connect(self.on_switch_to_data_clicked)
        self.db = Db.unit
        self.patDataNums = None
        self.patDataNumsAlreadyExists = False
        
        if self.patData != None:
            nums = self.db.getFirst('''SELECT * FROM "Patient_data" WHERE PatientId = %s ''', (patData[0]))
            self.patDataNumsAlreadyExists = nums != None
            if self.patDataNumsAlreadyExists:
                self.patDataNums = nums[2:-1]
        pass        
        
        
    def on_switch_to_data_clicked(self):
        self.patDataNumsWin = PatientDataWin(self, self.patDataNums)
        self.patDataNumsWin.show()
        self.patDataNumsWin.pushButton.clicked.connect(self.on_accept_pat_data_nums)
        pass
    
    def on_accept_pat_data_nums(self):
        self.patDataNums = [int(numBox.value()) for numBox in self.patDataNumsWin.findChildren(QDoubleSpinBox)]
        self.patDataNumsWin.close()
        pass
        