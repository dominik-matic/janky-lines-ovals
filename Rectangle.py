class Rectangle:
	def __init__(self, x: int, y: int, w: int, h: int):
		self._x = x
		self._y = y
		self._w = w
		self._h = h
	
	def getX(self):
		return self._x
	
	def getY(self):
		return self._y
	
	def getWidth(self):
		return self._w
	
	def getHeight(self):
		return self._h