# pyqt5 - ui
# другие библиотеки для логики

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from first import Ui_FirstDialog
from second import  Ui_SecondDialog

app = QtWidgets.QApplication(sys.argv)

FirstDialog = QtWidgets.QDialog()
ui = Ui_FirstDialog()
ui.setupUi(FirstDialog)
FirstDialog.show()

#logic..
def OpenSecondWindow():
    global SecondDialog
    SecondDialog = QtWidgets.QDialog()
    ui = Ui_SecondDialog()
    ui.setupUi(SecondDialog)
    FirstDialog.hide()
    SecondDialog.show()

    def ReturnToFirstWindow():
        SecondDialog.close()
        FirstDialog.show()

    ui.pushButton.clicked.connect(ReturnToFirstWindow)

ui.pushButton_2.clicked.connect(OpenSecondWindow)

sys.exit(app.exec_())
