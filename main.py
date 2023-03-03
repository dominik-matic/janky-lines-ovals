#!/bin/python3.9
from LineSegment import LineSegment
from Oval import Oval
from GUI import GUI

def main():
	objects = []
	objects.append(LineSegment())
	objects.append(Oval())

	gui = GUI(objects)
	gui.mainloop()

if __name__ == "__main__":
	main()	