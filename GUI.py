import tkinter as tk
from tkinter import filedialog as fd
from GraphicalObject import GraphicalObject
from DocumentModel import DocumentModel
from CanvasRenderer import CanvasRenderer
from DocumentModelListener import DocumentModelListener
from State import State
from IdleState import IdleState
from AddShapeState import AddShapeState
from SelectShapeState import SelectShapeState
from EraserState import EraserState
from Point import Point
from CompositeShape import CompositeShape
from SVGRenderer import SVGRenderer

class GUI(tk.Tk, DocumentModelListener):
	def __init__(self, objects: list[GraphicalObject]):
		super().__init__()
		self.title('Very cool software')
		self.geometry('800x600')
		self.initToolBar(objects)
		self.frame = tk.Frame(self)
		self.frame.pack(fill=tk.BOTH, expand=1)
		self.canvas = tk.Canvas(self.frame)
		self.initDict(objects) # za učitavanje
		self.model = DocumentModel()
		self.model.subscribe(self)
		self.state = IdleState()
		self.bindKeys()
		self.draw()

	def initToolBar(self, objects: list[GraphicalObject]):
		self.toolbar = tk.Frame(self, bd=1, relief=tk.FLAT)
		for o in objects:
			btn = tk.Button(self.toolbar, text=o.getShapeName(), command=lambda o=o: self.setAddShapeState(o) , relief=tk.FLAT)
			btn.pack(side=tk.LEFT, padx=2, pady=2)

		btn = tk.Button(self.toolbar, text='Selektiraj', command=self.setSelectState, relief=tk.FLAT)
		btn.pack(side=tk.LEFT, padx=2, pady=2)
		btn = tk.Button(self.toolbar, text='Brisalo', command=self.setEraserState, relief=tk.FLAT)
		btn.pack(side=tk.LEFT, padx=2, pady=2)
		btn = tk.Button(self.toolbar, text='SVG Export', command=self.SVGExport, relief=tk.FLAT)
		btn.pack(side=tk.LEFT, padx=2, pady=2)
		btn = tk.Button(self.toolbar, text='Pohrani', command=self.saveCanvas, relief=tk.FLAT)
		btn.pack(side=tk.LEFT, padx=2, pady=2)
		btn = tk.Button(self.toolbar, text='Učitaj', command=self.loadCanvas, relief=tk.FLAT)
		btn.pack(side=tk.LEFT, padx=2, pady=2)
		
		self.toolbar.pack(side=tk.TOP, fill=tk.X)

	def bindKeys(self):
		self.bind('<Escape>', self.setDefaultState)
		self.canvas.bind('<Button-1>', lambda event: self.state.mouseDown(Point(event.x, event.y), False, False))
		self.canvas.bind('<Control-Button-1>', lambda event: self.state.mouseDown(Point(event.x, event.y), False, True))
		self.canvas.bind('<Shift-Button-1>', lambda event: self.state.mouseDown(Point(event.x, event.y), True, False))
		self.canvas.bind('<Control-Shift-Button-1>', lambda event: self.state.mouseDown(Point(event.x, event.y), True, True))
		self.canvas.bind('<ButtonRelease-1>', lambda event: self.state.mouseUp(Point(event.x, event.y), False, False))
		self.canvas.bind('<Control-ButtonRelease-1>', lambda event: self.state.mouseUp(Point(event.x, event.y), False, True))
		self.canvas.bind('<Shift-ButtonRelease-1>', lambda event: self.state.mouseUp(Point(event.x, event.y), True, False))
		self.canvas.bind('<Control-Shift-ButtonRelease-1>', lambda event: self.state.mouseUp(Point(event.x, event.y), True, True))
		self.canvas.bind('<B1-Motion>', lambda event: self.state.mouseDragged(Point(event.x, event.y)))
		self.bind('<Key>', lambda event: self.state.keyPressed(event.keysym))

	def initDict(self, objects: list[GraphicalObject]):
		self.objDict = dict()
		for o in objects:
			id = o.getShapeID().split(' ')[0]
			self.objDict[id] = o
		self.objDict['@COMP'] = CompositeShape([], False)

	def setDefaultState(self, event):
		self.state.onLeaving()
		self.state = IdleState()

	def setAddShapeState(self, prototype):
		self.state.onLeaving()
		self.state = AddShapeState(self.model, prototype)
	
	def setSelectState(self):
		self.state.onLeaving()
		self.state = SelectShapeState(self.model)

	def setEraserState(self):
		self.state.onLeaving()
		self.state = EraserState(self.model, self)

	def SVGExport(self):
		filename = fd.asksaveasfilename(defaultextension='.svg')
		if(filename is None):
			return
		svgrenderer = SVGRenderer(filename)
		for o in self.model.getObjects():
			o.render(svgrenderer)
		svgrenderer.close()
		
	def saveCanvas(self):
		file = fd.asksaveasfile(mode='w', defaultextension='.txt')
		if file is None:
			return
		rows = []
		for o in self.model.getObjects():
			o.save(rows)
		file.writelines(rows)
		file.close()
	
	def loadCanvas(self):
		rows = []
		stack = []
		file = fd.askopenfile()
		if file is None:
			return
		for line in file:
			rows.append(line)
		for line in rows:
			splitted = line.split(' ')
			id = splitted[0]
			data = splitted[1:]
			self.objDict[id].load(stack, data)
		
		self.model = DocumentModel()
		self.model.subscribe(self)
		for o in stack:
			self.model.addGraphicalObject(o)

		

	def documentChange(self):
		self.draw()

	def draw(self):
		r = CanvasRenderer(self.canvas)
		self.canvas.delete('all')
		for o in self.model.getObjects():
			o.render(r)	
			self.state.afterDraw(r, o)
		self.state.afterDrawEverything(r)
		self.canvas.pack(fill=tk.BOTH, expand=1)


