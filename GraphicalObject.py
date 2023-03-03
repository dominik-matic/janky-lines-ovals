from Renderer import Renderer
from Point import Point

class GraphicalObject:
	# podrška za uređivanje objekta
	def isSelected(self): pass
	def setSelected(self, selected): pass
	def getNumberOfHotPoints(self): pass
	def getHotPoint(self, index): pass
	def setHotPoint(self, index, point: Point): pass
	def isHotPointSelected(self, index): pass
	def setHotPointSelected(self, index, selected): pass
	def getHotPointDistance(self, index, mousePoint: Point): pass
	
	# geometrijska operacija nad oblikom
	def translate(self, delta: Point): pass
	def getBoundingBox(self): pass
	def selectionDistance(self, mousePoint: Point): pass

	# podrška za crtanje
	def render(self, r: Renderer): pass

	# observer za dojavu promjena modelu
	def addGraphicalObjectListener(self, l): pass
	def removeGraphicalObjectListener(self, l): pass

	# podrška za prototip (alatna traka, stvaranja obketata u crtežu)
	def getShapeName(self): pass
	def duplicate(self): pass

	# podrška za snimanje i učitavanje
	def getShapeID(self): pass
	def load(self, stack, data): pass
	def save(self, rows): pass