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

import FreeCAD, Part

class Rib:
	def __init__(self, obj):
		obj.Proxy = self
		pass

	def onChanged(self, fp, prop):
		"Do something when a property has changed"
		pass
			
	def execute(self, fp):
		"Print a short message when doing a recomputation, this method is mandatory" 
		pass

def makeRib(Shape):
	a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Rib")
	a.ViewObject.Proxy=0
	a.Shape = Shape.copy()
	Rib(a)
	FreeCAD.ActiveDocument.recompute()
	return a
