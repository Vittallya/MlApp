from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QLineEdit, QTextEdit, QMessageBox, QApplication, QMainWindow
from PyQt5.QtGui import QRegExpValidator
from Services.loginService import LoginService
from Services.Db import Db
#from Views import docWindow
import time
from Services.userService import UserService
from Views.docWindow import DocWindow
from Views.adminView import AdminWindow
from PyQt5.QtCore import QRegExp

qt_creator_file = "UI/startWin.ui"
Ui_Start_Window, QtBaseClassStart = uic.loadUiType(qt_creator_file)


class StartWindow(QtWidgets.QMainWindow, Ui_Start_Window):
    
    def __init__(self, app: QApplication):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Start_Window.__init__(self)
        self.setupUi(self)    
        self.passwordText.setEchoMode(QLineEdit.EchoMode.Password)    
        self.pushButton.clicked.connect(self.on_login_clicked)
        self.app = app
        self.loginService = LoginService(Db.unit)
        
        validator = QRegExpValidator(QRegExp(r"[\d\w]+"))
        self.pushButton.setEnabled(False)
        
        for lineEdit in self.findChildren(QLineEdit):
            lineEdit.setValidator(validator)
            lineEdit.textChanged.connect(self.on_line_edit_key_pressed)
        
        #self.model = TodoModel()
        #self.todoView.setModel(self.model)
        
    def is_all_line_edit_correct(self, lineEdits):
        return all([lineEdit.validator().validate(lineEdit.text(), 0)[0] == 2 for lineEdit in lineEdits])
        
    def on_line_edit_key_pressed(self, event):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(event, 0)[0]
        
        if state != 2:
            sender.setStyleSheet('QLineEdit { border: 1px solid red }')
        else:
            sender.setStyleSheet('')

        isOk = self.is_all_line_edit_correct(self.findChildren(QLineEdit))
        self.pushButton.setEnabled(isOk)
        # if state == QtGui.QValidator.Acceptable:
        #     color = '#c4df9b' # green
        # elif state == QtGui.QValidator.Intermediate:
        #     color = '#fff79a' # yellow
        # else:
        #     color = '#f6989d' # red
        # sender.setStyleSheet('QLineEdit { background-color: %s }' % color)
        
        pass
        
    def on_login_clicked(self):
        login = self.loginText.text()
        psw = self.passwordText.text()
        user = self.loginService.tryAuthentificate(login, psw)
            
        if user == None:
            QMessageBox(text='Пользователь не найден', parent=self).show()
        else:
            global window
            
            if user[2] == 'Врач':
                window = DocWindow(self.app, self)
            elif user[2] == 'Администратор':                            
                window = AdminWindow(self.app, self)
            else:
                raise Exception("Роль не определена")
            UserService.unit.setUser(user[0], user[4], user[2])
            self.app.setActiveWindow(window)
            window.load()
            window.show()
            self.hide()