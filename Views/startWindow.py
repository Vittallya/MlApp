from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QLineEdit, QTextEdit, QMessageBox, QApplication, QMainWindow
from PyQt6.QtCore import Qt
from Services.loginService import LoginService
from Services.Db import Db
from Views.docWindow import DocWindow
import time
from Services.userService import UserService

qt_creator_file = "UI/autWin.ui"
Ui_Start_Window, QtBaseClassStart = uic.loadUiType(qt_creator_file)


class StartWindow(QtWidgets.QDialog, Ui_Start_Window):
    
    def __init__(self, app: QApplication, docWin: QMainWindow, adminWin: QMainWindow):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Start_Window.__init__(self)
        self.setupUi(self)        
        self.pushButton.clicked.connect(self.on_login_clicked)
        self.app = app
        self.docWin = docWin
        self.adminWin = adminWin
        self.loginService = LoginService(Db.unit)
        #self.model = TodoModel()
        #self.todoView.setModel(self.model)
        
    def on_login_clicked(self):
        login = self.loginText.text()
        psw = self.passwordText.text()
        user = self.loginService.tryAuthentificate(login, psw)
            
        if user == None:
            QMessageBox(text='Пользователь не найден', parent=self).show()
        else:
            win = None
            
            if user[2] == 'Администратор':
                win = self.adminWin
            elif user[2] == 'Врач':                            
                win = self.docWin                
            else:
                raise Exception("Роль не определена")
            UserService.unit.setUser(user[0], user[2], user[4])
            
            win.show()
            win.load()
            self.close()