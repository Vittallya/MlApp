from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import sys
from Views.startWindow import StartWindow
from Views.docWindow import DocWindow
from Views.adminView import AdminWindow
from Services.Db import Db
from Services.userService import UserService

global window

if __name__ == "__main__":
    Db('qszocldx', 'qszocldx', 'tt-NUA1sSoy3p9oi8zw-YrNLQvGaOmdq', 'snuffleupagus.db.elephantsql.com')
    UserService(Db.unit)
    app = QApplication(sys.argv)    
    app.setQuitOnLastWindowClosed(True)
    win = StartWindow(app)
    win.show()


    sys.exit(app.exec())