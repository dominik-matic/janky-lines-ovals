from GraphicalObject import GraphicalObject
from AbstractGraphicalObject import AbstractGraphicalObject
from Rectangle import Rectangle
from Renderer import Renderer
from Point import Point

class CompositeShape(AbstractGraphicalObject):
	def __init__(self, shapes: list[GraphicalObject], selected):
		super().__init__([])
		self._shapes = shapes
		self._selected = selected

	def translate(self, delta: Point):
		for s in self._shapes:
			s.translate(delta)
		self.__notifyListeners__()

	def selectionDistance(self, mousePoint: Point):
		min = None
		for s in self._shapes:
			dist = s.selectionDistance(mousePoint)
			if(min is None or dist < min):
				min = dist
		return min

	def getBoundingBox(self):
		x1, y1, x2, y2 = None, None, None, None
		for s in self._shapes:
			bb = s.getBoundingBox()
			x = bb.getX()
			y = bb.getY()
			if(x1 is None or x < x1):
				x1 = x
			if(y1 is None or y < y1):
				y1 = y
			x = x + bb.getWidth()
			y = y + bb.getHeight()
			if(x2 is None or x > x2):
				x2 = x
			if(y2 is None or y > y2):
				y2 = y
		return Rectangle(x1, y1, x2 - x1, y2 - y1)

	
	def duplicate(self):
		myShapesCopy = []
		for s in self._shapes:
			myShapesCopy.append(s.duplicate())
		return CompositeShape(myShapesCopy, self.isSelected())

	def getShapeName(self):
		return "Kompozit"

	def getShapes(self):
		return self._shapes

	def render(self, r: Renderer):
		for s in self._shapes:
			s.render(r)

	def getShapeID(self):
		return '@COMP ' + len(self._shapes) 
	
	def load(self, stack, data):
		toPop = int(data[0])
		shapes = []
		for _ in range(toPop):
			shapes.append(stack.pop())
		newComp = CompositeShape(shapes, False)
		stack.append(newComp)
	
	def save(self, rows):
		for s in self._shapes:
			s.save(rows)
		rows.append(self.getShapeID() + '\n')