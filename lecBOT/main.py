# pyqt5 - ui
# другие библиотеки для логики

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from first import Ui_FirstDialog
from second import  Ui_SecondDialog
import webbrowser
import time

#запуск начального окна
app = QtWidgets.QApplication(sys.argv)
FirstDialog = QtWidgets.QDialog()
ui = Ui_FirstDialog()
ui.setupUi(FirstDialog)
FirstDialog.show()

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

    ui.pushButton.clicked.connect(ReturnToFirstWindow)#save new subj

ui.pushButton_2.clicked.connect(OpenSecondWindow)#add new subj

def BotStart(): #первый запуск бота
    link = 'www.google.com'  # url website
    alarm = '19:32:00'  # lec start
    Current_time = '00:00:00'
    while (Current_time != alarm):
        #print("Waiting, the current time is " + Current_time)  # to the console
        Current_time = time.strftime("%H:%M:%S")
        time.sleep(1)  # every sec

    if (Current_time == alarm):  # open website
        print("Starting Lecture")
        webbrowser.open(link)

ui.pushButton_6.clicked.connect(BotStart())


sys.exit(app.exec_())
