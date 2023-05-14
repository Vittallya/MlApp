from UI.patientVerdictWin import Ui_Dialog
from PyQt5 import QtWidgets

class VerdictWin(QtWidgets.QDialog, Ui_Dialog):
    
    def __init__(self, state, recs, acc, parent) -> None:
        QtWidgets.QDialog.__init__(self, parent)
        #Ui_Verdict_Dialog.__init__(self)
        self.setupUi(self)
        
        self.lb_state.setText(state)
        self.lb_recs.setText(recs)
        self.lb_acc.setText(str(acc))
        self.bt_accept.clicked.connect(self.on_accept_clicked)
        
        
    def on_accept_clicked(self):
        self.close()
        