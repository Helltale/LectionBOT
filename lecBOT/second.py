# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondDialog(object):
    def setupUi(self, SecondDialog):
        SecondDialog.setObjectName("SecondDialog")
        SecondDialog.resize(830, 312)
        self.groupBox = QtWidgets.QGroupBox(SecondDialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 10, 721, 111))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(30, 30, 151, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 60, 151, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(200, 30, 151, 31))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(200, 60, 151, 31))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setGeometry(QtCore.QRect(370, 30, 151, 31))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_6.setGeometry(QtCore.QRect(370, 60, 151, 31))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_7.setGeometry(QtCore.QRect(540, 30, 151, 31))
        self.radioButton_7.setObjectName("radioButton_7")
        self.groupBox_2 = QtWidgets.QGroupBox(SecondDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 130, 721, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_8.setGeometry(QtCore.QRect(30, 20, 151, 41))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_9.setGeometry(QtCore.QRect(30, 70, 151, 41))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_10.setGeometry(QtCore.QRect(200, 20, 151, 41))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_11 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_11.setGeometry(QtCore.QRect(200, 70, 151, 41))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_12 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_12.setGeometry(QtCore.QRect(370, 20, 151, 41))
        self.radioButton_12.setObjectName("radioButton_12")
        self.radioButton_13 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_13.setGeometry(QtCore.QRect(370, 70, 151, 41))
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_14 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_14.setGeometry(QtCore.QRect(540, 20, 151, 41))
        self.radioButton_14.setObjectName("radioButton_14")
        self.radioButton_15 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_15.setGeometry(QtCore.QRect(540, 70, 151, 41))
        self.radioButton_15.setObjectName("radioButton_15")
        self.label = QtWidgets.QLabel(SecondDialog)
        self.label.setGeometry(QtCore.QRect(40, 260, 71, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(SecondDialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 260, 291, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(SecondDialog)
        self.pushButton.setGeometry(QtCore.QRect(430, 260, 121, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(SecondDialog)
        QtCore.QMetaObject.connectSlotsByName(SecondDialog)

    def retranslateUi(self, SecondDialog):
        _translate = QtCore.QCoreApplication.translate
        SecondDialog.setWindowTitle(_translate("SecondDialog", "Add"))
        self.groupBox.setTitle(_translate("SecondDialog", "День недели"))
        self.radioButton.setText(_translate("SecondDialog", "Понедельник"))
        self.radioButton_2.setText(_translate("SecondDialog", "Вторник"))
        self.radioButton_3.setText(_translate("SecondDialog", "Среда"))
        self.radioButton_4.setText(_translate("SecondDialog", "Четверг"))
        self.radioButton_5.setText(_translate("SecondDialog", "Пятница"))
        self.radioButton_6.setText(_translate("SecondDialog", "Суббота"))
        self.radioButton_7.setText(_translate("SecondDialog", "Воскресенье"))
        self.groupBox_2.setTitle(_translate("SecondDialog", "Время пары"))
        self.radioButton_8.setText(_translate("SecondDialog", "08:00\n"
"09:35"))
        self.radioButton_9.setText(_translate("SecondDialog", "09:45\n"
"11:20"))
        self.radioButton_10.setText(_translate("SecondDialog", "11:30\n"
"13:05"))
        self.radioButton_11.setText(_translate("SecondDialog", "13:30\n"
"15:05"))
        self.radioButton_12.setText(_translate("SecondDialog", "15:15\n"
"16:50"))
        self.radioButton_13.setText(_translate("SecondDialog", "17:00\n"
"18:35"))
        self.radioButton_14.setText(_translate("SecondDialog", "18:45\n"
"20:15"))
        self.radioButton_15.setText(_translate("SecondDialog", "20:25\n"
"21:55"))
        self.label.setText(_translate("SecondDialog", "ФИО"))
        self.pushButton.setText(_translate("SecondDialog", "Сохранить"))



