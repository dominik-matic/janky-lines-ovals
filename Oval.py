from AbstractGraphicalObject import AbstractGraphicalObject
from Rectangle import Rectangle
from Point import Point
from Renderer import Renderer
import GeometryUtil
from math import pi, sin, cos, sqrt

class Oval(AbstractGraphicalObject):
	def __init__(self, p1: Point = Point(40, 0), p2: Point = Point(0, 40)):
		super().__init__([p1, p2])

	def selectionDistance(self, mousePoint: Point):
		rect = self.getBoundingBox()
		if(	mousePoint.getX() > rect.getX() and mousePoint.getX() < rect.getX() + rect.getWidth()
		and	mousePoint.getY() > rect.getY() and mousePoint.getY() < rect.getY() + rect.getHeight()):
			return 0

		x1 = rect.getX()
		y1 = rect.getY()
		w = rect.getWidth()
		h = rect.getHeight()

		A = Point(x1, y1)
		B = A.translate(Point(w, 0))
		C = A.translate(Point(0, h))
		D = A.translate(Point(w, h))

		dist1 = GeometryUtil.distanceFromLineSegment(A, B, mousePoint)
		dist2 = GeometryUtil.distanceFromLineSegment(A, C, mousePoint)
		dist3 = GeometryUtil.distanceFromLineSegment(B, C, mousePoint)
		dist4 = GeometryUtil.distanceFromLineSegment(C, D, mousePoint)
		
		return min(dist1, dist2, dist3, dist4)
		
	
	def getBoundingBox(self):
		p0 = self.getHotPoint(0)
		p1 = self.getHotPoint(1)
		x1 = p0.getX()
		y1 = p1.getY()

		x2 = x1 - (x1 - p1.getX()) * 2
		y2 = y1 - (y1 - p0.getY()) * 2

		x = x1 if x1 < x2 else x2
		y = y1 if y1 < y2 else y2

		w = abs(p0.getX() - p1.getX()) * 2
		h = abs(p0.getY() - p1.getY()) * 2

		return Rectangle(x, y, w, h)

	def duplicate(self):
		return Oval(self.getHotPoint(0), self.getHotPoint(1))

	def getShapeName(self):
		return "Oval"

	def render(self, r: Renderer):
		points = []
		bb = self.getBoundingBox()
		a = bb.getWidth() / 2
		b = bb.getHeight() / 2
		centerX = bb.getX() + a
		centerY = bb.getY() + b
		
		for i in range(180):
			kut = (2 * pi) * (i + 1) / 180
			sinKut = sin(kut)
			cosKut = cos(kut)
			radius = a * b / sqrt(a**2 * sinKut**2 + b**2 * cosKut**2)
			x = int(centerX + radius * cosKut + 0.5)
			y = int(centerY + radius * sinKut + 0.5)
			points.append(Point(x, y))
		
		r.fillPolygon(points)


	def getShapeID(self):
		x1 = str(self.getHotPoint(0).getX())
		y1 = str(self.getHotPoint(0).getY())
		x2 = str(self.getHotPoint(1).getX())
		y2 = str(self.getHotPoint(1).getY())
		return '@OVAL {} {} {} {}'.format(x1, y1, x2, y2)

	def load(self, stack, data):
		newOval = Oval(
			Point(int(data[0]), int(data[1])),
			Point(int(data[2]), int(data[3]))
		)
		stack.append(newOval)
	
	def save(self, rows):
		rows.append(self.getShapeID() + '\n')
