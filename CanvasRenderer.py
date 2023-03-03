from Point import Point
from Renderer import Renderer
from tkinter import Canvas

class CanvasRenderer(Renderer):
	def __init__(self, canvas: Canvas):
		self._canvas = canvas
	
	def drawLine(self, s: Point, e : Point):
		self._canvas.create_line(s.getX(), s.getY(), e.getX(), e.getY(), fill='blue')

	def fillPolygon(self, points: list[Point]):
		pointList = []
		for p in points:
			pointList.append(p.getX())
			pointList.append(p.getY())
		self._canvas.create_polygon(pointList, fill='blue', outline='red')			
