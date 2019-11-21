#Domnika Popov
#Home scene file
#10/10/19

import lsystem as ls
import shapes as s
import turtle_interpreter as ti 
import tree as t

def main(): 
	'''creates the home scene by calling shape functions at different line styles'''
	terp = ti.TurtleInterpreter()
	
	r = s.Rectangle(50)
	r.setStyle('jitter3')
	r.setJitter(3)
	r.setColor('lawn green')
	r.draw(-400,-400, 1.5, 90)
	
	r = s.Rectangle(50)
	r.setStyle('jitter3')
	r.setJitter(3)
	r.setColor('light sky blue')
	r.draw(-400,0, 1.5, 90)
	
	r = s.Rectangle(20)
	r.setStyle('jitter')
	r.setJitter(3)
	r.setColor('light slate blue')
	r.draw(-250,-180, 6, 90)
	
	sq = s.Square(180)
	sq.setStyle('jitter')
	sq.setJitter(3)
	sq.setColor('light slate blue')
	sq.draw(-250,120)
	
	rt = s.Rectangle(20)
	rt.setStyle('jitter')
	rt.setJitter(2)
	rt.setColor('grey')
	rt.draw(-240,210)
	
	tr = s.Triangle(45)
	tr.setStyle('jitter')
	tr.setJitter(3)
	tr.setColor('dark slate blue')
	tr.draw(-250,120, 4, 60)
	
	rt = s.Rectangle(40)
	rt.setStyle('jitter')
	rt.setJitter(2)
	rt.setColor('dark slate blue')
	rt.draw(-220,-20)
	
	sq = s.Square(80)
	sq.setStyle('jitter')
	sq.setJitter(3)
	sq.setColor('slate blue')
	sq.draw(-220,100)
	
	sq = s.Square(90)
	sq.setStyle('jitter')
	sq.setJitter(3)
	sq.setColor('slate blue')
	sq.draw(100,30)
	
	sq = s.Square(90)
	sq.setStyle('jitter')
	sq.setJitter(3)
	sq.setColor('slate blue')
	sq.draw(-40,30)

	t.Tree1 = t.Tree(distance = 10, color = (0.1, 0.5, 0.3), filename = 'systemDL.txt')
	t.Tree1.draw(290,-90 )
	t.Tree2 = t.Tree(distance = 15, color = (0.1, 0.5, 0.3), filename = 'systemFL.txt')
	t.Tree2.draw(-320,-90)

	terp.hold()

if __name__ == "__main__":
	main()