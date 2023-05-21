from PyQt5.QtWidgets import QDialog, QDoubleSpinBox, QLineEdit
from Services.Db import Db
from Services.Db import Db
from UI.patientEditWin import Ui_Dialog
from Views.patientDataWin import PatientDataWin
from Services.Db import Db
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

class PatientEditWin(QDialog, Ui_Dialog):
    
    def __init__(self, parent, emps, patData = None) -> None:
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.isEdit = patData != None
        self.patData = patData
        self.btSwitchToData.clicked.connect(self.on_switch_to_data_clicked)
        self.db = Db.unit
        self.patDataNums = None
        self.patDataNumsAlreadyExists = False
        self.btAccept.setEnabled(self.isEdit)
        selectedIndex = None
        
        self.cmDoctors.clear()
        self.patNumsId = None
        
        lines = self.findChildren(QLineEdit)
        
        for line in lines:
            line.textChanged.connect(self.text_changed)
        
        for index, emp in enumerate(emps):
            self.cmDoctors.addItem(str(emp[1]), emp[0])            
            if selectedIndex == None and patData != None and patData[4] == emp[0]:
                selectedIndex = index
        
        if self.patData != None:
            nums = self.db.getFirst('''SELECT * FROM "Patient_data" WHERE PatientId = %s ''', (patData[0],))
            self.patDataNumsAlreadyExists = nums != None
            
            if self.patDataNumsAlreadyExists:
                self.patNumsId = nums[0]
                self.patDataNums = nums[2:-2]
                
            if selectedIndex != None:
                self.cmDoctors.setCurrentIndex(selectedIndex)
                
            self.editName.setText( patData[1])
            self.editLastName.setText(patData[2])
            self.editMidName.setText(patData[3])
        pass        
        
        
    def text_changed(self, text):
        sender = self.sender()
        #validator = sender.validator()
        validator = QRegExpValidator(QRegExp(r'.+'))
        state = validator.validate(text, 0)[0]
        
        if state != 2:
            sender.setStyleSheet('QLineEdit { border: 1px solid red }')
        else:
            sender.setStyleSheet('')

        childs = self.findChildren(QLineEdit)          
        allCorrect = all([validator.validate(line.text(), 0)[0] == 2 for line in childs])
        
        self.btAccept.setEnabled(allCorrect)       
        
        
    def on_switch_to_data_clicked(self):
        self.patDataNumsWin = PatientDataWin(self, self.patDataNums)
        self.patDataNumsWin.show()
        self.patDataNumsWin.pushButton.clicked.connect(self.on_accept_pat_data_nums)
        pass
    
    def on_accept_pat_data_nums(self):
        self.patDataNums = [int(numBox.value()) for numBox in self.patDataNumsWin.findChildren(QDoubleSpinBox)]
        self.patDataNumsWin.close()
        pass
        