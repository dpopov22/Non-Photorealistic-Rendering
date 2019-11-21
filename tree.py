#Domnika Popov
#Tree file
#10/10/19

import lsystem as ls
import shapes as s
import turtle_interpreter as t 
import random

class Tree(s.Shape):
	'''creates a new type of object, allowing new instances of that type to be made, 
	a tree in this case, using the parent function of shapes'''
	def __init__(self, distance=5, angle=22.5, color=(0.5, 0.4, 0.3), iterations=3, filename=None):
		s.Shape.__init__(self, distance = distance, angle = angle, color = color , istring = '')
		self.iterations= iterations
		self.filename = filename
		self.lsystem = ls.Lsystem(self.filename)
		
	def setIterations(self, iterations):
		'''sets the iterations'''
		self.iterations = iterations 
	
	def read(self, filename):
		'''reads in the filename'''
		ls.Lsystem.read(filename)
	
	def draw(self, xpos, ypos, scale=1.0, orientation=0):
		'''allows for the tree to be drawn'''
		self.istring = self.lsystem.buildString(self.iterations)
		s.Shape.setString(self, self.istring)
		s.Shape.draw(self, xpos, ypos, scale=1.0, orientation=90)

def main(): 
	'''calls the different trees'''
	Tree1 = Tree(distance = 5, color = (0.1, 0.5, 0.3), filename = 'systemDL.txt')
	Tree1.draw(100, -200)
	Tree2 = Tree(distance = 10, color = (0.1, 0.5, 0.3), filename = 'systemFL.txt')
	Tree2.draw(0, -200)
	Tree3 = Tree(distance = 15, color = (0.1, 0.5, 0.3), filename = 'systemDL.txt')
	Tree3.draw(-100, -200)
	terp = t.TurtleInterpreter()
	
	
	terp.hold()

if __name__ == "__main__":
	main()