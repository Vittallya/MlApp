from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtSql import QSqlDatabase, QSqlDriver, QSqlTableModel
import sys
from Views.startWindow import StartWindow
from Views.docWindow import DocWindow
from Views.adminView import AdminWindow
from Services.Db import Db
from Services.userService import UserService

if __name__ == "__main__":
    Db('qszocldx', 'qszocldx', 'tt-NUA1sSoy3p9oi8zw-YrNLQvGaOmdq', 'snuffleupagus.db.elephantsql.com')
    UserService(Db.unit)
    app = QApplication(sys.argv)    
    app.setQuitOnLastWindowClosed(True)
    docWin = DocWindow()
    adminWin = AdminWindow
    win = StartWindow(app, docWin, adminWin)
    win.show()
    
    
    sys.exit(app.exec())