from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QHeaderView
from UI.coefsWin import Ui_Dialog
import pandas as pd
import numpy as np

class CoefsWin(QDialog, Ui_Dialog):
    
    def __init__(self, parent, data:dict) -> None:
        super().__init__(parent)
        self.setupUi(self)
        
        df = pd.DataFrame(data['coefficients'])
        self.coefsTable.setRowCount(df.shape[0])
        self.coefsTable.setColumnCount(df.shape[1])
        self.coefsTable.setHorizontalHeaderLabels(df.columns)
        self.coefsTable.setVerticalHeaderLabels(df.index.astype(str))
        self.coefsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iloc[i, j]))
                self.coefsTable.setItem(i, j, item)
                
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(len(data['bias']))
        for index, b in enumerate(data['bias']):
            self.tableWidget.setItem(0, index, QTableWidgetItem(str(b)))