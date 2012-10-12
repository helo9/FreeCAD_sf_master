#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2012                                              		*  
#*   Jonathan Hahn <>                            									*  
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

import FreeCAD, FreeCADGui, os
import Draft
import Part
import sys
from PyQt4 import QtGui,QtCore 
import Airfoil

mw = QtGui.qApp.activeWindow()

class MakeAirfoil:
	def Activated(self):
		from Gui import AirfoilDialog
		
		sel = Draft.getSelection()[0]
		
		Shape = 0
		
		if(sel.Type != 'Part::Part2DObjectPython' and sel.Type != 'Part::FeaturePython'):
			QtGui.QMessageBox.critical(mw,"Invalid Selection", "You must select 'Part::Part2DObjectPython'",QtGui.QMessageBox.Ok)
			return
		
		try:
			Shape = sel.Shape
		except Exception, e:
			return
		
		#create Airfoil
		af = Airfoil.makeAirfoil(Shape)
		
		#show Dialog
		result = AirfoilDialog.AirfoilDialog.showDialog(af.Length,af.Thickness,0,0,0)
		
		if(result is None):
			FreeCAD.ActiveDocument.removeObject(af.Name)
		else:
			af.Length = result[0]
			af.Thickness = result[1]
			af.Placement = FreeCAD.Placement(FreeCAD.Vector(result[2],result[3],result[4]),FreeCAD.Rotation())
			sel.ViewObject.Visibility = False

	def IsActive(self):
		if(len(Draft.getSelection())==1):
			return True
		else:
			return False

	def GetResources(self):
		#IconPath = Paths.iconsPath() + "/Ico.png"
		MenuText = str('Create Airfoil')
		ToolTip  = str('Create an Airfoil, from any Wired Object')
		return {'MenuText': MenuText, 'ToolTip': ToolTip}
class MakeWing:
	def Activated(self):
		import Wing
		from Gui import WingDialog
		aviableAirfoils = []
		for obj in FreeCAD.ActiveDocument.Objects:
			if(obj.Type == 'Part::FeaturePython'):
				if(obj.Proxy.__module__ == 'Airfoil'):
					aviableAirfoils.append(obj.Name)
		result = WingDialog.WingDialog.showDialog(aviableAirfoils,None)
		
		if(result == None):
			return
		elif(result == []):
			return
		
		objlist = []
		for name in result:
			FreeCAD.ActiveDocument.getObject(name).ViewObject.Visibility = False
			objlist.append(FreeCAD.ActiveDocument.getObject(name))
		
		Wing.makeWing(objlist)
		
	def IsActive(self):
		if(FreeCAD.ActiveDocument != None):
			return True
		else:
			return False
			
	def GetResources(self):
		#IconPath = Paths.iconsPath() + "/Ico.png"
		MenuText = str('Create Wing')
		ToolTip  = str('Create an Wing, from Airfoils')
		return {'MenuText': MenuText, 'ToolTip': ToolTip}

class MakeRibbedWing:
	def Activated(self):
		import RibbedWing
		from Gui import RibbedWingDialog
		wing = 0
		sel = Draft.getSelection()
		#must be Wing
		if(len(sel)==1):		
			if(sel[0].Type == 'Part::FeaturePython'):
				if(sel[0].Proxy.__module__ == 'Wing'):
					RibbedWing.makeRibbedWing(sel[0])
		#must be Airfoils
		elif(len(sel)>1):
			Airfoils = []
			for obj in sel:
				if(obj.Type == 'Part::FeaturePython'):
					if(obj.Proxy.__module__ == 'Airfoil'):
						Airfoils.append(obj.Shape)
			if(len(Airfoils)>1):
				import Wing
				wing = Wing.makeWing(Airfoils)
				RibbedWing.makeRibbedWing(wing)
			#TODO else error
		#TODO else error
		
	def IsActive(self):
		if(len(Draft.getSelection())>=1):
			return True
		else:
			return False
			
	def GetResources(self):
		#IconPath = Paths.iconsPath() + "/Ico.png"
		MenuText = str('Create Ribbed-Wing')
		ToolTip  = str('Create an Ribbed-Wing, from Wing')
		return {'MenuText': MenuText, 'ToolTip': ToolTip}

FreeCADGui.addCommand('Wing_makeAirfoil', MakeAirfoil())
FreeCADGui.addCommand('Wing_MakeWing',MakeWing())
FreeCADGui.addCommand('Wing_makeRibbedWing',MakeRibbedWing())
