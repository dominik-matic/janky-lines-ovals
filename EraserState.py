from State import State
from Point import Point

class EraserState(State):
	def __init__(self, model, gui):
		self.model = model
		self.gui = gui
		self.erasingLine = []
		self.lineIds = []
		self.toDelete = []
	
	def mouseDragged(self, mousePoint: Point):
		objs = self.model.findSelectedGraphicalObject(mousePoint)
		for o in objs:
			if(o not in self.toDelete):
				self.toDelete.append(o)
		if(len(self.erasingLine) > 0):
			x0 = self.erasingLine[-1].getX()
			y0 = self.erasingLine[-1].getY()
			x1 = mousePoint.getX()
			y1 = mousePoint.getY()
			id = self.gui.canvas.create_line(x0, y0, x1, y1, fill='blue')
			self.lineIds.append(id)
		self.erasingLine.append(mousePoint)
		self.gui.draw

	def mouseUp(self, mousePoint: Point, shoftDown: bool, ctrlDown: bool):
		self.erasingLine.clear()
		for id in self.lineIds:
			self.gui.canvas.delete(id)
		for o in self.toDelete:
			if(o in self.model.getObjects()):
				self.model.getObjects().remove(o)
		self.toDelete.clear()
		self.gui.draw()
		