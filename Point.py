class Point:
	def __init__(self, x: int, y: int):
		self._x = x
		self._y = y
	
	def getX(self):
		return self._x
	
	def getY(self):
		return self._y
	
	def translate(self, dp: 'Point'):
		return Point(self._x + dp.getX(), self._y + dp.getY())
	
	def difference(self, p: 'Point'):
		return Point(self._x - p.getX(), self._y - p.getY())
