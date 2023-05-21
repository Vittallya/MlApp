from UI.patientData import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QDoubleSpinBox
from PyQt5 import Qt


class PatientDataWin(QDialog, Ui_Dialog):
    
    
    def __init__(self, parent, patDataNums = None, readOnly = False) -> None:
        super().__init__(parent)
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.isEdit = patDataNums != None
        self.patDataNums = patDataNums
        
        allNumBoxes = self.findChildren(QDoubleSpinBox)
        
        if(patDataNums != None):
            for i in range(0, len(patDataNums)):
                allNumBoxes[i].setValue(int(patDataNums[i]))
                allNumBoxes[i].setEnabled(not readOnly)
        
        pass
    
    