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

from __future__ import division
import FreeCAD, Draft, Part
import Wing, Rib

class RibbedWing:
	def __init__(self, obj):
		obj.addProperty("App::PropertyLink","WingShape","Base","The Wing Shape")
		obj.addProperty("App::PropertyBool", "LeadingEdge", "Base", "En-/Disables Leading Edge")
		obj.addProperty("App::PropertyBool", "TrailingEdge", "Base", "En-/Disables Trailing Edge")
		obj.addProperty("App::PropertyLinkList","Ribs","Base","Rib Objects")
		obj.addProperty("App::PropertyInteger","Number","Ribs","How many ribs the Wing should have")
		obj.addProperty("App::PropertyLength", "RibThickness", "Ribs", "Thickness of Ribs")

		obj.Proxy = self
		
	def onChanged(self, obj, prop):
		pass
		
	def execute(self, obj):
		pass
	
	def createGeometry(self, obj):
		'''Create Ribs, Edges a.s.o.'''
		
		#return if Properties are missing
		if(not hasattr(obj, "WingShape") or not hasattr(obj, "Number") or not hasattr(obj, "RibThickness")):
			return			
		
		direction = None
		
		if(not hasattr(obj.WingShape, "Direction")):
			z = obj.WingShape.Shape.BoundBox.ZLength
			direction = FreeCAD.Vector(0,0,z)
		else:
			direction = obj.WingShape.Direction
		
		#define Start Point
		x = obj.WingShape.Shape.BoundBox.XMin
		y = obj.WingShape.Shape.BoundBox.YMin
		z = obj.WingShape.Shape.BoundBox.ZMin
		
		start = FreeCAD.Vector(x,y,z)
		
		#define lenght, hight
		length = obj.WingShape.Shape.BoundBox.XLength
		hight = obj.WingShape.Shape.BoundBox.YLength
		
		number = obj.Number
		thickness = obj.RibThickness
		
		#call createBoxes
		boxes = self.getBoxes(start, direction, number, length, hight, thickness)
		
		#TODO leading trailing edge etc
		
		#create Ribs
		counter = 0
		
		ribs = []
		
		for box in boxes:
			counter = counter+1
			
			FreeCAD.Console.PrintMessage("creates Rib "+str(counter)+"/"+str(len(boxes))+"...")
			
			tempribshape = obj.WingShape.Shape.common(box)
			
			tempribobj = Rib.makeRib(tempribshape)
			
			ribs.append(tempribobj)
			
			FreeCAD.Console.PrintMessage(" done \n")
			
			FreeCAD.ActiveDocument.recompute()
			
		obj.Ribs = ribs
		
		
			
	def getBoxes(self, start, direction, number, length, hight, thickness):
		'''creates Boxes for common operation with WingShape to get Ribs'''
		
		FreeCAD.Console.PrintMessage(	"Daten:"+str(direction)+"\n")
		
		boxes = []
		
		distance = FreeCAD.Vector(direction)
		distance.multiply(1/(number-1))
		
		halfthicknessvec = FreeCAD.Vector(direction)
		halfthicknessvec.normalize()
		halfthicknessvec.multiply(thickness/2)
		
		thicknessvec = FreeCAD.Vector(direction)
		thicknessvec.normalize()
		thicknessvec.multiply(thickness)
		
		normdir = FreeCAD.Vector(direction)
		normdir.normalize()
		
		#create first box
		boxes.append(Part.makeBox(length,hight,thickness,start,normdir))
		
		position = start
		
		#create boxes in middle
		for i in range(1, number-1):
			position = position + distance
			boxes.append(Part.makeBox(length,hight,thickness,position-halfthicknessvec,normdir))
	
		#create last box
		boxes.append(Part.makeBox(length,hight,thickness,start+direction-thicknessvec,normdir))
	
		return boxes

class ViewProvider_RibbedWing:
	'''ViewProvider for RibbedWing'''
	def __init__(self, vobj):
		vobj.Proxy = self
		self.Object = vobj.Object
	
	def attach(self, vobj):
		'''Function called during load-process'''
		vobj.Proxy = self
		self.Object = vobj.Object
		
	def claimChildren(self, vobj):
		return self.Object.WingShape

def makeRibbedWing(WingShape, Number, RibThickness):
	'''make a Ribbed Wing'''
	
	a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Rib")
	
	RibbedWing(a)
	
	a.WingShape = WingShape
	a.Number = Number
	a.RibThickness = RibThickness
	
	a.Proxy.createGeometry(a)
	
	FreeCAD.ActiveDocument.recompute()
