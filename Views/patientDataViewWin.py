from UI.patientDataViewTable import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QLabel, QHeaderView, QTableWidgetItem
from Views.patientDataWin import PatientDataWin


class PatientDataViewWin(QDialog, Ui_Dialog):
    
    def __init__(self, parent, patData) -> None:
        super().__init__(parent)
        self.setupUi(self)
        
        p = PatientDataWin(parent)
        self.columns = [label.text() for label in p.findChildren(QLabel)]
        p.close()
        
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setRowCount(len(patData))
        self.tableWidget.setColumnCount(2)
        
        for index, value in enumerate(patData):
            self.tableWidget.setItem(index, 0, QTableWidgetItem(self.columns[index]))
            self.tableWidget.setItem(index, 1, QTableWidgetItem(str(value)))