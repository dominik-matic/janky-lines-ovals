from GraphicalObjectListener import GraphicalObjectListener
from GraphicalObject import GraphicalObject
from DocumentModelListener import DocumentModelListener
from Point import Point

class DocumentModel:
	SELECTION_PROXIMITY = 10

	class GOListener(GraphicalObjectListener):
		def __init__(self, outer):
			self.outer = outer
		def graphicalObjectChanged(self, go: GraphicalObject):
			self.outer.notifyListeners()
		def graphicalObjectSelectionChanged(self, go: GraphicalObject):
			if(go.isSelected()):
				if(go not in self.outer._selectedObjects):
					self.outer.getSelectedObjects().append(go)
			else:
				if(go in self.outer._selectedObjects):
					self.outer.getSelectedObjects().remove(go)
			self.outer.notifyListeners()

	
	def __init__(self):
		self._objects = []
		#self._roObjects
		self._listeners = []
		self._selectedObjects = []
		#self.roSelectedObjects
		self._goListener = self.GOListener(self)

	def clear(self):
		for obj in self._objects:
			obj.removeGraphicalObjectListener(self)
		self._objects.clear()
		self._selectedObjects.clear()

	def addGraphicalObject(self, obj):
		self._objects.append(obj)
		if(obj.isSelected()):
			self._selectedObjects.append(obj)
		obj.addGraphicalObjectListener(self._goListener)
		self.notifyListeners()

	def removeGraphicalObject(self, obj: GraphicalObject):
		self._objects.remove(obj)
		if obj in self._selectedObjects:
			self._selectedObjects.remove(obj)
		obj.removeGraphicalObjectListener(self._goListener)
		self.notifyListeners()
	
	def notifyListeners(self):
		for l in self._listeners:
			l.documentChange()

	def getObjects(self):
		return self._objects

	def getSelectedObjects(self):
		return self._selectedObjects

	def clearSelectedObjects(self):
		for o in self._selectedObjects:
			o.setSelected(False, notify=False)
		self._selectedObjects.clear()
		self.notifyListeners()

	def addSelectedObject(self, obj: GraphicalObject):
		obj.setSelected(True)
		self._selectedObjects.append(obj)
		self.notifyListeners()

	def increaseZ(self, go: GraphicalObject):
		size = len(self._objects)
		index = -1
		try:
			index = self._objects.index(go)
		except:
			print('increaseZ: No such object')

		if(index == size - 1):
			return

		self._objects.insert(index + 1, self._objects.pop(index))
		self.notifyListeners()

	def decreaseZ(self, go: GraphicalObject):
		index = -1
		try:
			index = self._objects.index(go)
		except:
			print('decreaseZ: No such object')

		if(index == 0):
			return

		self._objects.insert(index - 1, self._objects.pop(index))
		self.notifyListeners()

	def findSelectedGraphicalObject(self, mousePoint: Point):
		ret = []
		for obj in self._objects:
			distance = obj.selectionDistance(mousePoint)
			if(distance <= self.SELECTION_PROXIMITY):
				ret.append(obj)
		return ret

	def findSelectedHotPoint(self, obj: GraphicalObject, mousePoint: Point):
		index = -1
		for i in range(obj.getNumberOfHotPoints()):
			distance = obj.getHotPointDistance(i, mousePoint)
			if(distance <= self.SELECTION_PROXIMITY):
				index = i
				break
		return index

	def subscribe(self, l: DocumentModelListener):
		self._listeners.append(l)
	
	def unsubscribe(self, l: DocumentModelListener):
		self._listeners.remove(l)
	

