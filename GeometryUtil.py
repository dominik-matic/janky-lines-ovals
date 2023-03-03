from Point import Point
from math import sqrt, dist

def distanceFromPoint(p1: Point, p2: Point):
	a = dist([p1.getX(), p1.getY()], [p2.getX(), p2.getY()])
	return a

# thank you stack overflow
def distanceFromLineSegment(s: Point, e: Point, p: Point):
	A = p.getX() - s.getX()
	B = p.getY() - s.getY()
	C = e.getX() - s.getX()
	D = e.getY() - s.getY()

	dot = A * C + B * D
	lsq = C * C + D * D
	param = -1
	if(lsq != 0):
		param = dot / lsq
	
	xx, yy = 0, 0
	if(param < 0):
		xx = s.getX()
		yy = s.getY()
	elif(param > 1):
		xx = e.getX()
		yy = e.getY()
	else:
		xx = s.getX() + param * C
		yy = s.getY() + param * D
	
	dx = p.getX() - xx
	dy = p.getY() - yy
	return sqrt(dx * dx + dy * dy)