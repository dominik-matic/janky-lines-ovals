from GraphicalObjectListener import GraphicalObjectListener
from GraphicalObject import GraphicalObject
import GeometryUtil
from Point import Point

class AbstractGraphicalObject(GraphicalObject):
	def __init__(self, points: list[Point]):
		self._hotPoints = points
		self._selected = False
		self._listeners = []
		self._hotPointsSelected = []
		for _ in points:
			self._hotPointsSelected.append(False)
	
	def getHotPoint(self, index: int):
		return self._hotPoints[index]
	
	def setHotPoint(self, index: int, p: Point):
		self._hotPoints[index] = p # can throw exception
		self.__notifyListeners__()
	
	def getNumberOfHotPoints(self):
		return len(self._hotPoints)

	def getHotPointDistance(self, index, mousePoint: Point):
		return GeometryUtil.distanceFromPoint(self._hotPoints[index], mousePoint)

	def isHotPointSelected(self, index):
		return self._hotPointsSelected[index]

	def setHotPointSelected(self, index, selected):
		self._hotPointsSelected[index] = selected

	def isSelected(self):
		return self._selected

	def setSelected(self, selected, notify=True):
		self._selected = selected
		if(notify):
			self.__notifySelectionListeners__()

	def translate(self, delta: Point):
		self._hotPoints[:] = [p.translate(delta) for p in self._hotPoints]
		self.__notifyListeners__()

	def addGraphicalObjectListener(self, l : GraphicalObjectListener):
		self._listeners.append(l)
	def removeGraphicalObjectListener(self, l: GraphicalObjectListener):
		self._listeners.remove(l)

	def __notifyListeners__(self):
		for l in self._listeners:
			l.graphicalObjectChanged(self)
			
	
	def __notifySelectionListeners__(self):
		for l in self._listeners:
			l.graphicalObjectSelectionChanged(self)