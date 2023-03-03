from Point import Point
from State import State
from Renderer import Renderer
from DocumentModel import DocumentModel
from GraphicalObject import GraphicalObject
from CompositeShape import CompositeShape

class SelectShapeState(State):
	def __init__(self, model: DocumentModel):
		self.model = model

	def mouseDown(self, mousePoint: Point, shiftDown: bool, ctrlDown: bool):
		if(not ctrlDown):
			self.model.clearSelectedObjects()
		obj = self.model.findSelectedGraphicalObject(mousePoint)
		if(len(obj) == 0):
			return
		obj[-1].setSelected(not obj[-1].isSelected())

	def mouseDragged(self, mousePoint: Point):
		obj = self.model.findSelectedGraphicalObject(mousePoint)
		if(len(obj) == 0):
			return
		i = -1
		target = None
		for o in obj:
			target = o
			i = self.model.findSelectedHotPoint(o, mousePoint)
		if(i == -1):
			return
		target.setHotPoint(i, mousePoint)

	def keyPressed(self, keyCode):
		objs = self.model.getSelectedObjects()
		if(len(objs) == 0):
			return
		if(keyCode == 'Up'):
			for o in objs:
				o.translate(Point(0, -1))
		elif(keyCode == 'Down'):
			for o in objs:
				o.translate(Point(0, 1))
		elif(keyCode == 'Left'):
			for o in objs:
				o.translate(Point(-1, 0))
		elif(keyCode == 'Right'):
			for o in objs:
				o.translate(Point(1, 0))
		elif(len(objs) == 1):
			if(keyCode == 'KP_Add' or keyCode == 'plus'):
				self.model.increaseZ(objs[0])
			elif(keyCode == 'KP_Subtract' or keyCode == 'minus'):
				self.model.decreaseZ(objs[0])
			elif(keyCode == 'u' or keyCode == 'U'):
				o = objs[0]
				if(isinstance(o, CompositeShape)):
					shapes = o.getShapes()
					self.model.getObjects().remove(o)
					self.model.getSelectedObjects().remove(o)
					for s in shapes:
						s.setSelected(True, notify=False)
						self.model.addGraphicalObject(s)
		else:
			if(keyCode == 'g' or keyCode == 'G'):
				newObjs = []
				for o in objs:
					newObjs.append(o)
				for o in objs:
					self.model.getObjects().remove(o)
				self.model._selectedObjects.clear()
				cs = CompositeShape(newObjs, True)
				self.model.addGraphicalObject(cs)
				

	def afterDraw(self, r: Renderer, go: GraphicalObject):
		if(not go.isSelected()):
			return
		
		bb = go.getBoundingBox()
		x = bb.getX()
		y = bb.getY()
		h = bb.getHeight()
		w = bb.getWidth()
		r.drawLine(Point(x, y), Point(x, y + h))
		r.drawLine(Point(x, y), Point(x + w, y))
		r.drawLine(Point(x + w, y), Point(x + w, y + h))
		r.drawLine(Point(x, y + h), Point(x + w, y + h))

		if(len(self.model.getSelectedObjects()) > 1):
			return
		
		for i in range(go.getNumberOfHotPoints()):
			p = go.getHotPoint(i)
			x = p.getX()
			y = p.getY()
			a = 5
			r.drawLine(Point(x - a, y - a), Point(x - a, y + a))
			r.drawLine(Point(x - a, y - a), Point(x + a, y - a))
			r.drawLine(Point(x + a, y + a), Point(x - a, y + a))
			r.drawLine(Point(x + a, y + a), Point(x + a, y - a))

	def onLeaving(self):
		self.model.clearSelectedObjects()
