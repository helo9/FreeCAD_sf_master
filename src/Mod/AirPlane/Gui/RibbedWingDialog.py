import sys
import PyQt4.QtGui
import FreeCAD
from PyQt4.QtGui import QDialog
from Ui_RibbedWingDialog import Ui_RibbedWingDialog

class RibbedWingDialog(QDialog):
	'''Dialog to Choose Airfoils'''
	def __init__(self,parent):
		QDialog.__init__(self)
		
		# Set up Ui from Designer
		self.ui = Ui_RibbedWingDialog()
		self.ui.setupUi(self)
		
		#Connect List
		self.ui.RibNumberSpin.valueChanged.connect(self.ValueChanged)
		self.ui.ThicknessSpin.valueChanged.connect(self.ValueChanged)
		
		self.NumberofRibs = 0
		self.RibThickness = 0
	def ValueChanged(self,value):
		self.NumberofRibs = self.ui.RibNumberSpin.value()
		self.RibThickness = self.ui.ThicknessSpin.value()
	def getResults(self):
		return [self.NumberofRibs,self.RibThickness]
	@staticmethod
	def showDialog(parent=None):
		dialog = RibbedWingDialog(parent)
		result = dialog.exec_()
		if result == QDialog.Accepted:
			return dialog.getResults()
		else:
			return None
		
		
	

