from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QApplication, QMainWindow, QDialog, QComboBox
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

class PatientEditWin(QDialog, Ui_Dialog):
    
    def __init__(self, parent, patientData = None) -> None:
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.isEdit = patientData != None
        self.patientData = patientData
        self.cmDoctors
        
            
    