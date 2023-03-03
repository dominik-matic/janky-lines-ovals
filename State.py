from GraphicalObject import GraphicalObject
from Renderer import Renderer
from Point import Point

class State:
	def mouseDown(self, mousePoint: Point, shiftDown: bool, ctrlDown: bool):
		pass

	def mouseUp(self, mousePoint: Point, shiftDown: bool, ctrlDown: bool):
		pass

	def mouseDragged(self, mousePoint: Point):
		pass

	def keyPressed(self,keyCode: int):
		pass

	def afterDraw(self, r: Renderer, go: GraphicalObject):
		pass
	
	def afterDrawEverything(self, r: Renderer):
		pass
	
	def onLeaving(self):
		pass

	