from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QLineEdit, QTextEdit, QMessageBox
from PyQt6.QtCore import Qt
from Services.docService import DocService
from Services.Db import Db

qt_creator_file_admin_window = "UI/docWin.ui"
Ui_Admin_Window, QtBaseClassAdmin = uic.loadUiType(qt_creator_file_admin_window)


class AdminWindow(QtWidgets.QMainWindow, Ui_Admin_Window):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Admin_Window.__init__(self)
        self.setupUi(self)
        self.docService = DocService(Db.unit)