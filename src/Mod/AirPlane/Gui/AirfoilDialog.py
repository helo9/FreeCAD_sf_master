import sys
import PyQt4.QtGui
import FreeCAD
from PyQt4.QtGui import QDialog
from Ui_AirfoilDialog import Ui_AirfoilDialog

class AirfoilDialog(QDialog):
	'''Dialog to Choose Airfoils'''
	def __init__(self,parent):
		QDialog.__init__(self)
		
		# Set up Ui from Designer
		self.ui = Ui_AirfoilDialog()
		self.ui.setupUi(self)
		
		#Connect List
		self.ui.buttonBox.accepted.connect(self.saveandaccept)
				
		self.Length = 0
		self.Thickness = 0
		self.x = 0
		self.y = 0
		self.z = 0
	def setLength(Length):
		self.Length = Length
	def setThickness(Thickness):
		self.Thickness = Thickness
	def saveandaccept(self):
		self.Length = self.ui.spin_length.value()
		self.Thickness = self.ui.spin_thickness.value()
		self.x = self.ui.spin_x.value()
		self.y = self.ui.spin_y.value()
		self.z = self.ui.spin_z.value()
		self.accept()
	def getResults(self):
		return [self.Length,self.Thickness,self.x,self.y,self.z]
	def setValues(self,Length, Thickness, x, y, z):
		ui = self.ui
		ui.spin_length.setValue(Length)
		ui.spin_thickness.setValue(Thickness)
		ui.spin_x.setValue(x)
		ui.spin_y.setValue(y)
		ui.spin_z.setValue(z)
	@staticmethod
	def showDialog(Length, Thickness, x, y, z, parent=None):
		dialog = AirfoilDialog(parent)
		dialog.setValues(Length, Thickness, x, y, z)
		result = dialog.exec_()
		if result == QDialog.Accepted:
			return dialog.getResults()
		else:
			return None
