#Domnika Popov
#Shapes File
#10/10/19

import turtle_interpreter as t 
class Shape:
	'''creates a new type of object, allowing new instances of that type to be made '''
	
	def __init__(self, distance = 100, angle = 90, color = (0, 0, 0), istring = '') :
		'''sets up the fields of a class and give them reasonable initial value'''
		self.distance = distance
		self.angle = angle 
		self.color = color 
		self.istring = istring 
		self.style = 'normal'
		self.jitterSigma = 2 
		self.linewidth = 1
		self.dotSize = 1
	
	def setColor(self,c):
		'''sets the color'''
		self.color = c
	
	def setDistance(self, d):
		'''sets the distance'''
		self.distance= d 
		
	def setAngle(self, a):
		'''sets the angle'''
		self.angle = a
	
	def setString(self, s):
		'''sets the string'''
		self.istring = s 
		
	def setStyle(self, s):
		'''sets style'''
		self.style=s
	
	def setJitter(self, j):
		'''sets jitter'''
		self.jitterSigma = j
	
	def setDotSize(self, d):
		'''sets dot size'''
		self.dotSize = d
	
	def setWidth(self, w):
		'''sets width'''
		self.linewidth = w
		
	def draw(self, xpos, ypos, scale=1.0, orientation=0):
		'''draws the object at a given position, size, and orientation'''	
		object = t.TurtleInterpreter()
		object.place(xpos, ypos, orientation)
		object.color(self.color)
		object.setStyle(self.style)
		object.setJitter(self.jitterSigma)
		object.setDotSize(self.dotSize)
		object.width(self.linewidth)
		object.drawString(self.istring, self.distance*scale, self.angle)
	
class Square(Shape):
	'''creates a filled square shape using the parent function'''
	def __init__(self, distance=100, clr=(0, 0, 0), xpos = 0, ypos = 0):
		Shape.__init__(self, distance=distance, angle = 90, color=clr, istring= '{F-F-F-F-}')
		
class UnfilledSquare(Shape):
	'''creates an unfilled square shape using the parent function'''
	def __init__(self, distance=100, clr=(0, 0, 0), xpos = 0, ypos = 0):
		Shape.__init__(self, distance=distance, angle = 90, color=clr, istring= 'F-F-F-F-')

class Rectangle(Shape):
	'''creates a filled rectangle shape using the parent function'''
	def __init__(self, distance=100, clr=(0, 0, 0), xpos = 0, ypos = 0):
		Shape.__init__(self, distance=distance, angle = 90, color=clr, istring= '{FF-FF----FF-FF--+FFFF}')

class Rectangle2(Shape):
	'''creates another version of the rectangle shape using the parent function'''
	def __init__(self, distance=100, clr=(0, 0, 0), xpos = 0, ypos = 0):
		Shape.__init__(self, distance=distance, angle = 90, color=clr, istring= 'FF-FF----FF-FF--+FFFF')

class UnfilledTriangle(Shape):
	'''creates an unfilled triangle shape using the parent function'''
	def __init__(self, distance=100, clr=(0, 0, 0), xpos = 0, ypos = 0):
		Shape.__init__(self, distance=distance, angle = 120, color=clr, istring= 'F-F-F-')

class Triangle(Shape):
	'''creates a filled triangle shape using the parent function'''
	def __init__(self, distance=100, clr=(0, 0, 0), xpos = 0, ypos = 0):
		Shape.__init__(self, distance=distance, angle = 120, color=clr, istring= '{F-F-F-}')
		
class Triangle2(Shape):
	'''creates a filled triangle shape using the parent function at a specific orientation'''
	def __init__(self, distance=100, clr=(0, 0, 0), xpos = 0, ypos = 0):
		Shape.__init__(self, distance=distance, angle = 120, color=clr, istring= '{F-F-F-}')
		Shape.draw(self, xpos, ypos, scale=1.0, orientation=0)	

class Triangle3(Shape):
	'''creates a filled triangle shape using the parent function at a specific orientation'''
	def __init__(self, distance=100, clr=(0, 0, 0), xpos = 0, ypos = 0):
		Shape.__init__(self, distance=distance, angle = 120, color=clr, istring= '{F-F-F-}')
		Shape.draw(self, xpos, ypos, scale=1.0, orientation=60) 

class Triangle4(Shape):
	'''creates a filled triangle shape using the parent function at a specific orientation'''
	def __init__(self, distance=100, clr=(0, 0, 0), xpos = 0, ypos = 0):
		Shape.__init__(self, distance=distance, angle = 120, color=clr, istring= '{F-F-F-}')
		Shape.draw(self, xpos, ypos, scale=1.0, orientation=30) 

class Triangle5(Shape):
	'''creates a filled triangle shape using the parent function at a specific orientation'''
	def __init__(self, distance=100, clr=(0, 0, 0), xpos = 0, ypos = 0):
		Shape.__init__(self, distance=distance, angle = 120, color=clr, istring= '{F-F-F-}')
		Shape.draw(self, xpos, ypos, scale=1.0, orientation=90) 

class Pentagon(Shape):
	'''creates a filled pentagon shape using the parent function at a specific orientation'''
	def __init__(self, distance=100, clr=(0, 0, 0), xpos = 0, ypos = 0 ):
		Shape.__init__(self, distance=distance, angle = 72, color=clr, istring= '{F-F-F-F-F-}')
		Shape.draw(self, xpos, ypos, scale=1.0, orientation=0)

class Hexagon(Shape):
	'''creates a filled hexagon shape using the parent function at a specific orientation'''
	def __init__(self, distance=100, clr=(0, 0, 0), xpos = 0, ypos = 0 ):
		Shape.__init__(self, distance=distance, angle = 60, color=clr, istring= '{F-F-F-F-F-F-}')
		Shape.draw(self, xpos, ypos, scale=1.0, orientation=0)

class Octagon(Shape):
	'''creates an unfilled octagon shape using the parent function at a specific orientation'''
	def __init__(self, distance=100, clr=(0, 0, 0), xpos = 0, ypos = 0 ):
		Shape.__init__(self, distance=distance, angle = 45 , color=clr, istring= 'F-F-F-F-F-F-F-F-')
		Shape.draw(self, xpos, ypos, scale=1.0, orientation=0)

class FilledOctagon(Shape):
	'''creates a filled octagon shape using the parent function at a specific orientation'''
	def __init__(self, distance=100, clr=(0, 0, 0), xpos = 0, ypos = 0 ):
		Shape.__init__(self, distance=distance, angle = 45 , color=clr, istring= '{F-F-F-F-F-F-F-F-}')
		Shape.draw(self, xpos, ypos, scale=1.0, orientation=0)

def main(): 
	'''calls the different shapes'''
	Hexagon(40, 'pink', -300, -100)
	Hexagon(50, 'pink', 0 , 100)
	Hexagon(40, 'pink', 235, 250)
	Pentagon(30, 'red', -300, 200)
	Pentagon(25, 'red', 10, 70)
	Pentagon(80, 'red', 250, -100)
	Octagon(70, 'green', 0, 150)
	Octagon(50, 'green', 225, 270)
	Octagon(50, 'green', -300, -80)
	terp = t.TurtleInterpreter()
	terp.hold()

if __name__ == "__main__":
	main()
	

