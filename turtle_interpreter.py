#Domnika Popov
#Turtle Interpreter File
#10/10/19

import turtle 
import random 
import sys 

class TurtleInterpreter:
	'''creates a new type of object, allowing new instances of that type to be made''' 
	initialized = False 
	def __init__(self, dx = 800, dy = 800):
		if TurtleInterpreter.initialized:
			return
		TurtleInterpreter.initialized = True
		turtle.setup(width = dx, height = dy)
		turtle.tracer(False)
		self.style = 'normal'
		self.jitterSigma =2 
		self.dotSize = 1
	
	def drawString(self, dstring, distance, angle):
		""" Interprets the characters in string dstring as a series
		of turtle commands. Distance specifies the distance
		to travel for each forward command. Angle specifies the
		angle (in degrees) for each right or left command. The list of 
		turtle supported turtle commands is:
		F : forward
		- : turn right
		+ : turn left
		"""
		'''allows for l systems to be drawn'''
		stack = []
		colorstack = []
		modval = None 
		modgrab = False 
		gravity = False 

		for c in dstring:
			if c =='(':
				modstring = ''
				modgrab = True
				continue 
			elif c == ')':
				modgrab = False
				modval = float(modstring)
				continue 
			elif modgrab == True: 
				modstring = modstring + c
				continue 
			if c == 'F':
				if modval == None:
					self.forward(distance)
				else: 
					self.forward(distance*modval)
			elif c == 'f':
				if modval == None:
					self.forward(distance)
				else:
					self.forward(distance*modval)
			elif c == '-':
				if gravity: 
					if quadrant: 
						if modval == None:
							turtle.right(angle*1.5)	  
						else: 
							turtle.right(modval*1.5)
					else: 
						if modval == None:
							turtle.right(angle*.5)	  
						else: 
							turtle.right(modval*.5)
				else:
					if modval == None:
						turtle.right(angle)	  
					else: 
						turtle.right(modval)
			elif c == '+':
				if modval == None:
					turtle.left(angle)
				else: 
					turtle.left(modval)
			elif c == '[':
				stack.append(turtle.position())
				stack.append(turtle.heading())
				#if the angle is in first or fourth quadrant make the angle larger 
				if turtle.heading() >=0 and turtle.heading() <=90: 
					gravity = True 
					quadrant = True
				#if the angle is in second or third quadrant make angle smaller 
				else: 
					gravity = True 
					quadrant = False
			elif c == ']':
				turtle.penup()
				turtle.setheading(stack.pop())
				turtle.goto(stack.pop())
				turtle.pendown()
			elif c == '<': 
				colorstack.append(turtle.color()[0])
			elif c =='>':
				turtle.color(colorstack.pop())
			elif c == 'g':
				turtle.color(0.15, 0.5, 0.2)	
			elif c == 'y': 
				turtle.color(0.8, 0.8, 0.3)
			elif c == 'r': 
				turtle.color(0.7, 0.2, 0.3)
			elif c == 'o':
				turtle.color('orange')
			elif c == 'p':
				turtle.color('hot pink')
			elif c == 't':
				turtle.color('dark turquoise')
			elif c == 'L':
				turtle.begin_fill()
				turtle.circle(distance, 180)
				turtle.end_fill()
			elif c =='B':
				turtle.begin_fill()
				turtle.circle(distance/3)
				turtle.end_fill()
			elif c == '{': 
				turtle.begin_fill()
			elif c == '}':
				turtle.end_fill()
			if c == '!':
				if modval == None: 
					w = turtle.width()
					if w > 1: 
						turtle.width(w-1)		  
				else: 
					turtle.width(modval)
			modval = None 
		turtle.update()
	
	def place(self, xpos, ypos, angle=None):
		'''places the turtle'''
		turtle.penup()
		turtle.goto(xpos, ypos)
		if angle != None: 
			self.orient(angle)
		turtle.pendown()
	
	def orient(self, angle):
		'''orients the turtle'''
		turtle.setheading(angle)
	
	def goto(self, xpos, ypos):
		'''gives the turtle a location'''
		turtle.penup()
		turtle.goto(xpos, ypos)
		turtle.pendown()
	
	def color(self, c):
		'''allows for the image to be colored'''
		turtle.color(c)
		
	def width(self, w):
		'''changes the width of the pen'''
		turtle.width(w)
	
	def setStyle(self, s):
		'''sets style of line'''
		self.style=s
	
	def setJitter(self, j):
		'''sets the jitter'''
		self.jitterSigma = j
	
	def setDotSize(self, d):
		'''sets the dot size'''
		self.dotSize = d

	def forward(self, distance):
		'''makes the turtle go forward'''
		if self.style == 'normal':
			turtle.forward(distance)
		elif self.style == 'jitter':
			(x0, y0) = turtle.position() 
			turtle.penup()
			turtle.forward(distance)
			(xf, yf) = turtle.position()
			curwidth = turtle.width()
			jx = random.gauss(0, self.jitterSigma)
			jy = random.gauss(0, self.jitterSigma)
			kx = random.gauss(0, self.jitterSigma)
			ky = random.gauss(0, self.jitterSigma)
			turtle.width(curwidth + random.randint(0, 2))
			turtle.goto(x0 + jx, y0 + jy)
			turtle.pendown()
			turtle.goto(xf + kx, yf + ky)
			turtle.penup()
			turtle.goto(xf, yf)
			turtle.width(curwidth)
			turtle.pendown()
		elif self.style == 'jitter3':
			for i in range(3): 
				(x0, y0) = turtle.position() 
				turtle.penup()
				turtle.forward(distance)
				(xf, yf) = turtle.position()
				curwidth = turtle.width()
				jx = random.gauss(0, self.jitterSigma)
				jy = random.gauss(0, self.jitterSigma)
				kx = random.gauss(0, self.jitterSigma)
				ky = random.gauss(0, self.jitterSigma)
				turtle.width(curwidth + random.randint(0, 2))
				turtle.goto(x0 + jx, y0 + jy)
				turtle.pendown()
				turtle.goto(xf + kx, yf + ky)
				turtle.penup()
				turtle.goto(xf, yf)
				turtle.width(curwidth)
				turtle.pendown()
		elif self.style == 'dotted': 
				(x0, y0) = turtle.position()
				numcircles = (distance/self.dotSize +1)
				for i in range(4): 
					turtle.color(random.random(), random.random(), random.random())
					turtle.dot(self.dotSize)
					turtle.penup()
					turtle.forward(distance*2)
					turtle.pendown()
	
	def ground(self, x, y, scale, col):
		'''This draws a ground background at (x,y) of the given scale and color'''
		turtle.tracer(0)
		turtle.setheading(0)
		turtle.penup()
		turtle.goto(x, y)
		turtle.pendown()
		turtle.color(col)
		turtle.begin_fill()
		turtle.forward(300*scale)
		turtle.left(90)
		turtle.forward(150*scale)
		turtle.left(90)
		turtle.forward(300*scale)
		turtle.left(90)
		turtle.forward(150*scale)
		turtle.end_fill()
		turtle.left(90) 
	
	def sky(self, x, y, scale, col):
		'''This draws a sky background at (x,y) of the given scale and color'''
		turtle.tracer(0)
		turtle.setheading(0)
		turtle.goto(x, y)
		turtle.color(col)
		turtle.begin_fill()
		turtle.forward(300*scale)
		turtle.left(90)
		turtle.forward(250*scale)
		turtle.left(90)
		turtle.forward(300*scale)
		turtle.left(90)
		turtle.forward(250*scale)
		turtle.end_fill()
		turtle.left(90)
	
	def hold(self):
		'''Holds the screen open until user clicks or presses 'q' key'''
		turtle.hideturtle()
		turtle.update()
		turtle.onkey(turtle.bye, 'q')
		turtle.listen()
		turtle.exitonclick()