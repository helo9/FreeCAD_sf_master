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

import FreeCAD, Draft, Part

class Airfoil:
	def __init__(self, obj):
		"App two point properties" 
		obj.addProperty("App::PropertyLength","Length","Airfoil","Length").Length=obj.Shape.BoundBox.XLength
		obj.addProperty("App::PropertyFloat","Thickness","Airfoil","Thickness").Thickness=obj.Shape.BoundBox.YLength/obj.Shape.BoundBox.XLength
		obj.Proxy = self
		self.changed = False

	def onChanged(self, fp, prop):
		"Do something when a property has changed"
		try:
			if(not fp.Shape.isValid()):
				return
		except:
			return
		if(fp.Shape is None):
			return
		FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
		if(prop == 'Length' or prop == 'Thickness'):
			#save Position
			Placement = fp.Placement.copy()
			
			#copy Shape
			TempShape = fp.Shape.copy()
			#set on standard position for scaling
			TempShape.Placement = FreeCAD.Placement(FreeCAD.Vector(0,0,0),FreeCAD.Rotation())
			fp.Placement = FreeCAD.Placement(FreeCAD.Vector(0,0,0),FreeCAD.Rotation())
			
			#abort if wrong values entered
			if(fp.Length <= 0 or fp.Thickness <= 0 or (fp.Length == TempShape.BoundBox.XLength and fp.Thickness == TempShape.BoundBox.YLength/TempShape.BoundBox.XLength) ):
				pass
			else:
				#calculate scalefactors - length and thickness
				scalefactor = fp.Length/TempShape.BoundBox.XLength
				scalefactorthickness = (fp.Thickness*TempShape.BoundBox.XLength)/TempShape.BoundBox.YLength
				mat = FreeCAD.Matrix()
				mat.scale(scalefactor,scalefactor*scalefactorthickness,0)
			
				#scale Shape
				TempShape = fp.Shape.transformGeometry(mat)
			
				#update shape
				fp.Shape =  TempShape
				self.changed = True
				
			fp.Placement = Placement
						
			FreeCAD.ActiveDocument.recompute()
			
	def execute(self, fp):
		"Print a short message when doing a recomputation, this method is mandatory" 
		pass

def makeAirfoil(Shape):
	a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Airfoil")
	a.ViewObject.Proxy=0
	a.Shape = Shape.copy()
	Airfoil(a)	
	FreeCAD.ActiveDocument.recompute()
	return a
