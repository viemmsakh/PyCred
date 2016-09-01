# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyCred_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(430, 200)
		Dialog.setMinimumSize(QtCore.QSize(430, 200))
		Dialog.setMaximumSize(QtCore.QSize(430, 200))
		Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(20, 0, 181, 41))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(Dialog)
		self.label_2.setGeometry(QtCore.QRect(20, 30, 301, 16))
		self.label_2.setObjectName("label_2")
		self.line = QtWidgets.QFrame(Dialog)
		self.line.setGeometry(QtCore.QRect(20, 50, 391, 16))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.label_3 = QtWidgets.QLabel(Dialog)
		self.label_3.setGeometry(QtCore.QRect(20, 60, 401, 91))
		self.label_3.setText("")
		self.label_3.setPixmap(QtGui.QPixmap("password.png"))
		#background = self.resource_path("password.png")
		#print(background)
		#self.label_3.setPixmap(QtGui.QPixmap(background))
		self.label_3.setObjectName("label_3")
		self.lineUsername = QtWidgets.QLineEdit(Dialog)
		self.lineUsername.setEnabled(True)
		self.lineUsername.setGeometry(QtCore.QRect(108, 83, 190, 20))
		self.lineUsername.setFrame(False)
		self.lineUsername.setObjectName("lineUsername")
		self.linePassword = QtWidgets.QLineEdit(Dialog)
		self.linePassword.setEnabled(True)
		self.linePassword.setGeometry(QtCore.QRect(108, 112, 190, 20))
		self.linePassword.setFrame(False)
		self.linePassword.setEchoMode(QtWidgets.QLineEdit.Password)
		self.linePassword.setObjectName("linePassword")
		self.line_2 = QtWidgets.QFrame(Dialog)
		self.line_2.setGeometry(QtCore.QRect(20, 150, 391, 16))
		self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.pushButton = QtWidgets.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(260, 170, 75, 23))
		self.pushButton.setObjectName("pushButton")
		self.pushButton_2 = QtWidgets.QPushButton(Dialog)
		self.pushButton_2.setGeometry(QtCore.QRect(340, 170, 75, 23))
		self.pushButton_2.setObjectName("pushButton_2")

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Windows Security"))
		self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#0033bc;\">Network Authentication</span></p></body></html>"))
		self.label_2.setText(_translate("Dialog", "Please enter user credentials"))
		self.pushButton.setText(_translate("Dialog", "OK"))
		self.pushButton_2.setText(_translate("Dialog", "Cancel"))
	
if __name__ == "__main__":
    import sys
	
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

