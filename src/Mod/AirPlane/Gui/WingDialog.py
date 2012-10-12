import sys
import PyQt4.QtGui
from PyQt4.QtGui import QDialog
from Ui_WingDialog import Ui_WingDialog

class WingDialog(QDialog):
	'''Dialog to Choose Airfoils'''
	def __init__(self,parent):
		QDialog.__init__(self)
		
		# Set up Ui from Designer
		self.ui = Ui_WingDialog()
		self.ui.setupUi(self)
		
		#Connect Buttons
		self.ui.addButton.clicked.connect(self.addToList)
		self.ui.removeButton.clicked.connect(self.removeFromList)
		
		#
		self.Result = []
	def addToList(self):
		'''adds Airfoils from List with aviable into List of used Airfoils'''
		sel = self.ui.list_aviable.currentItem()
		self.ui.list_used.addItem(sel.clone())
		self.ui.list_aviable.takeItem(self.ui.list_aviable.currentRow())
		#append item 
		self.Result.append(str(sel.text()))
	def removeFromList(self):
		'''counterpart to addToList'''
		sel = self.ui.list_used.currentItem()
		self.ui.list_aviable.addItem(sel.clone())
		self.ui.list_used.takeItem(self.ui.list_used.currentRow())
		#generate new Result list
		self.Result = []
		for index in range(self.ui.list_used.count()):
			self.Result.append(str(self.ui.list_used.item(index).test()))
	def addAirfoil(self,af):
		self.ui.list_aviable.addItem(af)
	def getResults(self):
		'''returns items in used-airfoils-list'''
		return self.Result
		items = []
	@staticmethod
	def showDialog(Airfoils, parent=None):
		dialog = WingDialog(parent)
		for Airfoil in Airfoils:
			dialog.addAirfoil(Airfoil)
		result = dialog.exec_()
		if result == QDialog.Accepted:
			return dialog.getResults()
		else:
			return None
		
		
	

