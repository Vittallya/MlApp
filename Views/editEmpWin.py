from UI.editEmployeeWin import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QLineEdit, QComboBox



class EditEmployeeWin(QDialog, Ui_Dialog):
    
    def __init__(self, parent, empData = None) -> None:
        super().__init__(parent)
        Ui_Dialog.__init__(self)        
        self.setupUi(self)
        self.empData = empData
        self.isEdit = empData != None
        self.pushButton.clicked.connect(self.on_accept_clicked)
        if self.isEdit:
           self.toggle_boxes(False)
           self.cbChangeLoginPsw.setChecked(False)
           self.cbChangeLoginPsw.stateChanged.connect(self.state_changed)
        else:
            self.cbChangeLoginPsw.hide()
    
    def on_accept_clicked(self):
        pass
    
    def state_changed(self, checked):
        self.toggle_boxes(checked)
            
    def toggle_boxes(self, isVisible):
        
        if isVisible:
           self.boxLogin.show() 
           self.boxPsw.show()
           self.boxPswElse.show()
        else:
           self.boxLogin.hide() 
           self.boxPsw.hide()
           self.boxPswElse.hide()
           
        