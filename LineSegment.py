from AbstractGraphicalObject import AbstractGraphicalObject
from Rectangle import Rectangle
from Point import Point
from Renderer import Renderer
import GeometryUtil

class LineSegment(AbstractGraphicalObject):
	def __init__(self, p1: Point = Point(0, 0), p2: Point = Point(50, 0)):
		super().__init__([p1, p2])
	
	def selectionDistance(self, mousePoint: Point):
		return GeometryUtil.distanceFromLineSegment(self.getHotPoint(0), self.getHotPoint(1), mousePoint)

	def getBoundingBox(self):
		x1 = self.getHotPoint(0).getX()
		y1 = self.getHotPoint(0).getY()
		x2 = self.getHotPoint(1).getX()
		y2 = self.getHotPoint(1).getY()
		
		x = x1 if x1 < x2 else x2
		y = y1 if y1 < y2 else y2

		h = abs(y2 - y1)
		w = abs(x2 - x1)
		return Rectangle(x, y, w, h)

	def duplicate(self):
		return LineSegment(self.getHotPoint(0), self.getHotPoint(1))

	def getShapeName(self):
		return "Linija"

	def render(self, r: Renderer):
		r.drawLine(self.getHotPoint(0), self.getHotPoint(1))

	def getShapeID(self):
		x1 = str(self.getHotPoint(0).getX())
		y1 = str(self.getHotPoint(0).getY())
		x2 = str(self.getHotPoint(1).getX())
		y2 = str(self.getHotPoint(1).getY())
		return '@LINE {} {} {} {}'.format(x1, y1, x2, y2)
	
	def load(self, stack, data):
		newLine = LineSegment(
			Point(int(data[0]), int(data[1])),
			Point(int(data[2]), int(data[3]))
		)
		stack.append(newLine)
	
	def save(self, rows):
		rows.append(self.getShapeID() + '\n')