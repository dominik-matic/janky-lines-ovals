from State import State
from Point import Point
from DocumentModel import DocumentModel
from GraphicalObject import GraphicalObject

class AddShapeState(State):
	def __init__(self, model : DocumentModel, prototype: GraphicalObject):
		self.model = model
		self.prototype = prototype
	
	def mouseDown(self, mousePoint: Point, shiftDown: bool, ctrlDown: bool):
		shape = self.prototype.duplicate()
		shape.translate(mousePoint)
		self.model.addGraphicalObject(shape)