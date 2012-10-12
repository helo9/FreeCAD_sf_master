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

class Wing:
	def __init__(self, obj):
		obj.addProperty("App::PropertyLinkList","Airfoils","Base","The objects that make part of this cell")
		obj.addProperty("App::PropertyBool","Segmented","Wing","...")
		obj.addProperty("App::PropertyVectorList","LeadingPoints","peta","puta")
		obj.addProperty("App::PropertyVectorList","TrailingPoints","peta","puta")
		obj.Proxy = self
		
		self.changed = False
		
	def onChanged(self, fp, prop):
		pass
	
	def execute(self, fp):
		'''Called from doc.recompute'''
		needupdate = False
		
		for Airfoil in fp.Airfoils:
			if Airfoil.Proxy.changed:
				needupdate = True
				break
		
		if needupdate:
			self.createGeometry(fp)
			self.createCurves(fp)
			self.changed = True
		
	def createGeometry(self, fp):
		Airfoils = sortAirfoils(fp.Airfoils)
	
		Wires = []
	
		for Airfoil in Airfoils:
			Wires.append(Airfoil.Shape.Wires[0])
		
		Faces = []
		
		if(not fp.Segmented):
			FreeCAD.Console.PrintMessage("Create Normal Wing-Geometry\n")
			Loft = Part.makeLoft(Wires)
			
			Faces = Loft.Faces
			for Face in Faces:
				Face.reverse()
				
			RevertedShape = Airfoils[0].Shape.copy()
			RevertedShape.reverse()
			Faces.append(RevertedShape.Faces[0])
			Faces.append(Airfoils[-1].Shape.Faces[0])
	
		else:
			FreeCAD.Console.PrintMessage("Create Segmented Wing-Geometry\n")
			last = None
			
			
			
			for Wire in Wires:

				if(last is None):
					last = Wire
					continue
				
				WingSegment = Part.makeLoft([last,Wire])
				
				for Face in WingSegment.Faces:
					Face.reverse()
				
				Faces.extend(WingSegment.Faces)
				
				last = Wire
			
			RevertedShape = Airfoils[-1].Shape.copy()
			RevertedShape.reverse()
			Faces.append(RevertedShape.Faces[0])
			Faces.append(Airfoils[0].Shape.Faces[0])
			
		Shell = Part.makeShell(Faces)
		TempSolid = Part.makeSolid(Shell)			
		fp.Shape = Part.makeSolid(Shell)
		
		if(fp.Shape.Volume < 0):
			TempShape = fp.Shape.copy()
			TempShape.reverse()
			fp.Shape = TempShape
			
		
	
	def createCurves(self,fp):
	
		LeadingEdge_PointList = []
		
		TrailingEdge_PointList = []
		
		for Airfoil in fp.Airfoils:
			LeadingEdge_PointList.append(Airfoil.Shape.Vertexes[0].Point)
			
			lNo = len(Airfoil.Shape.Vertexes)/2
			TrailingEdge_PointList.append(Airfoil.Shape.Vertexes[lNo].Point)
					
		fp.LeadingPoints = LeadingEdge_PointList
		fp.TrailingPoints = TrailingEdge_PointList
			
	'''def getCurves_nor(self,lep,tep):
		return [Part.makePolygon(lep),Part.makePolygon(tep)]
							
	def getCurves_seg(self,lep,tep):		
		LeadingEdge_Spline = Part.BSplineCurve()
		TrailingEdge_Spline = Part.BSplineCurve()
		
		LeadingEdge_Spline.interpolate(lep)
		TrailingEdge_Spline.interpolate(tep)
		
		#fp.LeadingEdge = LeadingEdge_Spline.toShape()
		#fp.TrailingEdge = TrailingEdge_Spline.toShape()
		
		return [LeadingEdge_Spline.toShape(),TrailingEdge_Spline.toShape()]'''

class ViewProviderWing:
	def __init__(self, obj):
		"Set this object to the proxy object of the actual view provider"
		obj.Proxy = self
		self.Object = obj.Object
      
	def attach(self, obj):
		"Setup the scene sub-graph of the view provider, this method is mandatory"
		obj.Proxy = self
		self.Object = obj.Object
		
	def updateData(self, fp, prop):
		"If a property of the handled feature has changed we have the chance to handle this here"
		pass
		
	def getDisplayModes(self,obj):
		"Return a list of display modes."
		modes=[]
		return modes
		
	def getDefaultDisplayMode(self):
		"Return the name of the default display mode. It must be defined in getDisplayModes."
		return "Shaded"
		
	def getIcon(self):
         return """
				/* XPM */
				static char * Wing_xpm[] = {
				"32 32 19 1",
				" 	c None",
				".	c #393939",
				"+	c #553939",
				"@	c #AA3939",
				"#	c #C61C1C",
				"$	c #AA1C1C",
				"%	c #8E3939",
				"&	c #713939",
				"*	c #C60000",
				"=	c #551C39",
				"-	c #AA0000",
				";	c #551C1C",
				">	c #711C1C",
				",	c #8E0000",
				"'	c #710000",
				")	c #550000",
				"!	c #8E1C1C",
				"~	c #390000",
				"{	c #71001C",
				"                                ",
				"                                ",
				"           ..++.                ",
				"         +@####$%&.             ",
				"        &*********$&.           ",
				"        $***********#&=         ",
				"       .$*************$&        ",
				"       +#*************--+       ",
				"       +*************---;       ",
				"       &************---->       ",
				"       %************----,       ",
				"       $***********-----,+      ",
				"      .#**********-----,,;      ",
				"      +#**********-----,,;      ",
				"      &**********-----,,,'      ",
				"      &*********-----,,,,'.     ",
				"      %*********-----,,,'';     ",
				"      $********-----,,,,'';     ",
				"     +#*******-----,,,,''';     ",
				"     +#******-----,,,,''')'     ",
				"     &*******-----,,,''')))=    ",
				"     &******-----,,,,''')));    ",
				"     %*!;;;;>>>>>,,,''')))~;    ",
				"     %;!$$--$$$!!>>;;;{')~~)    ",
				"    .>--------,,,''';>>;;;;;.   ",
				"    .!$----$$$$!!!!>>>;=+++..   ",
				"      .+&+++...                 ",
				"                                ",
				"                                ",
				"                                ",
				"                                ",
				"                                "};
				"""
            
	def claimChildren(self):
		if(self.Object is not None):
			return self.Object.Airfoils
		else:
			return None
						
	def __getstate__(self):
		"When saving the document this object gets stored using Python's cPickle module.\
                Since we have some un-pickable here -- the Coin stuff -- we must define this method\
                to return a tuple of all pickable objects or None."
		return None
 
	def __setstate__(self,state):
		"When restoring the pickled object from document we have the chance to set some internals here.\
                Since no data were pickled nothing needs to be done here."				
		return None

def makeWing(Airfoils,Segments = False):
	'''creates Wing from Airfoils'''
	a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Wing")
	
	Wing(a)
	
	ViewProviderWing(a.ViewObject)
	a.Airfoils = sortAirfoils(Airfoils)
	a.Segmented = Segments
	
	a.Proxy.createGeometry(a)
	
	FreeCAD.ActiveDocument.recompute()
	
	return a

def sortAirfoils(Airfoils):
	#identify start point
	Airfoils = list(Airfoils)
	maxDistance = 0
	maxDistanceID = 0
	for i in range(0,len(Airfoils)-1):
		for Airfoil in Airfoils:
			Position1 = Airfoils[i].Placement.Base
			Position2 = Airfoil.Placement.Base
			
			if(Position1 == Position2):
				continue
			
			Distance = Position1.sub(Position2).Length
			
			if(Distance > maxDistance):
				maxDistance = Distance
				maxDistanceID = i
	#TODO:
	#if(maxDistance == 0):
	#	raise Exception()
	
	#sort Airfoils
	SortedAirfoils = []
	SortedAirfoils.append(Airfoils.pop(maxDistanceID))
	
	Distances = []
	Distances.append(0)
	
	StartPosition = SortedAirfoils[0].Placement.Base
	
	for Airfoil in Airfoils:
		CurAirfPos = Airfoil.Placement.Base
		
		DisFromStart = CurAirfPos.sub(StartPosition).Length
		
		correctPosition = 1
		
		while( correctPosition < len(Distances) ):
			if( Distances[correctPosition] > DisFromStart ):
				break
			correctPosition = correctPosition+1
		
		Distances.insert(correctPosition, DisFromStart)
		SortedAirfoils.insert(correctPosition, Airfoil)
	
	return SortedAirfoils
		
