from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QLineEdit, QTextEdit, QMessageBox, QApplication, QMainWindow
from Services.loginService import LoginService
from Services.Db import Db
#from Views import docWindow
import time
from Services.userService import UserService
from Views.docWindow import DocWindow
from Views.adminView import AdminWindow

qt_creator_file = "UI/startWin.ui"
Ui_Start_Window, QtBaseClassStart = uic.loadUiType(qt_creator_file)


class StartWindow(QtWidgets.QMainWindow, Ui_Start_Window):
    
    def __init__(self, app: QApplication):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Start_Window.__init__(self)
        self.setupUi(self)        
        self.pushButton.clicked.connect(self.on_login_clicked)
        self.app = app
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