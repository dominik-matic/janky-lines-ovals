from Renderer import Renderer
from Point import Point

class SVGRenderer(Renderer):
	def __init__(self, filename):
		self.filename = filename
		self.lines = list()
		self.lines.append('<svg version=\"1.1\" baseProfile=\"full\" width=\"800\" height=\"600\" xmlns=\"http://www.w3.org/2000/svg\">\n')

	def close(self):
		self.lines.append('</svg>')
		with open(self.filename, 'w') as file:
			file.writelines(self.lines)

	def drawLine(self, s: Point, e: Point):
		self.lines.append('<line x1=\"{}\" y1=\"{}\" x2=\"{}\" y2=\"{}\" style=\"stroke:blue;stroke-width:2\"/>\n'.format(s.getX(), s.getY(), e.getX(), e.getY()))

	def fillPolygon(self, points: list[Point]):
		pointsString = ""
		for p in points:
			pointsString += str(p.getX()) + ',' + str(p.getY()) + ' '
		pointsString = pointsString[:-1]
		self.lines.append('<polygon points=\"' + pointsString + '\" style=\"fill:blue;stroke:red\"/>\n')