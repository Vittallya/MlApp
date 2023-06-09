from UI.editEmployeeWin import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QLineEdit
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp


class EditEmployeeWin(QDialog, Ui_Dialog):
    
    def __init__(self, parent, roles, empData = None) -> None:
        super().__init__(parent)
        Ui_Dialog.__init__(self)        
        self.setupUi(self)
        self.empData = empData
        self.isEdit = empData != None
        selectedIndex = None
        self.editPassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.editPassword_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.prevLogin = None
        
        #self.editPassword.setValidator(QRegExpValidator(QRegExp(r"^(?=.*[0-9])(?=.*[a-z])([a-z0-9_-]+)$"), self.editPassword))
        #self.editPassword.keyPressed.connect(self.on_line_edit_key_pressed)
        
        #validator = QRegExpValidator(QRegExp(r"[\.]+"))
        self.pushButton.setEnabled(self.isEdit)
        
        for lineEdit in self.findChildren(QLineEdit):
            #lineEdit.setValidator(validator)
            lineEdit.textChanged.connect(self.on_line_edit_key_pressed)
        
        for index, role in enumerate(roles):
            self.cmRoles.addItem(str(role[1]), role[0])            
            if selectedIndex == None and self.isEdit and empData[6] == role[0]:
                selectedIndex = index
                self.cmRoles.setCurrentIndex(selectedIndex)
        self.empGuid = None
        if self.isEdit:
            self.prevLogin = empData[4]
            self.empGuid = empData[0]
            self.toggle_boxes(False)
            self.cbChangeLoginPsw.setChecked(False)
            self.cbChangeLoginPsw.stateChanged.connect(self.state_changed)
            self.editName.setText(empData[1])
            self.editSurname.setText(empData[2])
            self.editMidname.setText(empData[3])
            self.editLogin.setText(empData[4])            
        else:
            self.cbChangeLoginPsw.hide()   
    
    def on_line_edit_key_pressed(self, event):
        sender = self.sender()
        #validator = sender.validator()
        validator = QRegExpValidator(QRegExp(r'.+'))
        state = validator.validate(event, 0)[0]
        
        if state != 2:
            sender.setStyleSheet('QLineEdit { border: 1px solid red }')
        else:
            sender.setStyleSheet('')

        childsEmpData = self.frameEmpData.findChildren(QLineEdit)        
        childsUserData = self.frameUserData.findChildren(QLineEdit)        
        empCorrect = all([validator.validate(line.text(), 0)[0] == 2 for line in childsEmpData])
        userCorrect = all([validator.validate(line.text(), 0)[0] == 2 for line in childsUserData])
        
        self.pushButton.setEnabled(empCorrect and (userCorrect or self.isEdit and not self.cbChangeLoginPsw.isChecked()))       
        
    
    def state_changed(self, checked):
        self.toggle_boxes(checked)
            
    def toggle_boxes(self, isVisible):
        
        if isVisible:
           self.boxLogin_2.show() 
           self.boxPsw_2.show()
           self.boxPswElse_2.show()
        else:
           self.boxLogin_2.hide() 
           self.boxPsw_2.hide()
           self.boxPswElse_2.hide()
           
        