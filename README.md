# Non-Photorealistic-Rendering
In order to run this file, you will need python installed on your computer. To get the final result, 
please run the file “home.py”. The other files are the components that make up the final result. 
The purpose of this project was to use lsystems, a turtle interpreter, classes, inheritance, and 
new styles of drawing in order to create a scene in the style of cartoon art. A class is basically a 
template to create an object. They allow for less code to be written and for more complex images to be created. 
I made a shape class that was the "parent" function for more complex shapes, including trees. 
A parent class has a symbol table with methods that its "children" can inherit. 
The child classes inherit the methods from the parent class but can also have their own. 
Inheritance allows for more efficient coding because it means that it is not necessary to 
rewrite functions that will be needed for the child classes as well as the parent class.

The shape class basically allows for different shapes to be drawn and serves as the parent class. 
I had most of the classes that I created make a filled shape by using curly brackets to turn on and off the fill. 
I used the Shape class as the parent function to create a rectangle, octagon, hexagon, and pentagon. 

The tree shape class generates its string dynamically using an lsystem. I built a string using an l system 
every time I drew a tree and then used the shape draw method. The tree class is a child of the shape class, 
so it used the parent methods for setting color, distance, and angle. I created a Tree class by creating a file
called tree.py that imports the system and shape modules. I needed to override the init and draw method and 
create a set iterations method and a read method to create the tree class. The init method calls the parent init 
method with self, distance, angle, and color, and stored the iterations number in an iterations field. 
It also creates an lsystem object and stores it in an lsystem field. The draw method used the lsystem to build 
the string, assign the string to the string field of self, and then call the parent draw method. I made the default 
orientation 90 so that the trees would grow right side up.

My lsystem file reads in the lsystems, which create fractals by creating a base and a rule. 
The rule replaces parts of the base continuously to create fractals, which are similar patterns that recur
at progressively smaller scales. There are a number of setter and getter methods in the file that allow for 
this to occur, and comments are included in order to further explain the purpose of each function/method. 

The turtle interpreter file allows for l-systems to be drawn through a drawstring method, which supports branches 
and allows for a text string to be passed in. It interprets the characters in the passed- in string, which is a series 
of turtle commands. The distance specifies the distance that is traveled forward for each forward command, and the angle 
specifies the angle at which each left or right command is executed. This code is further explained in the actual file 
through comments.  I also had to implement new drawing styles, which were jitter, dotted, and jitter 3. These were 
implemented in my forward method.  I created the jitter methods by using several goto statements 
that had an offset of jx and jy. 
The jx and jy values were generated from a Gaussian distribution with a zero mean and jitterSigma as the standard deviation. 
The dotted style draws a series of circles separated by spaces.  
I had to create a field in the turtle interpreter that would hold the dot size and created a setDotSize method 
in the turtle interpreter class. I also needed to set a setDotSize method and make a dotSize field in the Shape class. 
The number of circles was equal to the distance divided by the dot size plus one. 


My home file basically just called all of the different shape classes from the shape file and the two different lsystem tree 
files to create a scene. I created a new type of rectangle that could be drawn at a different orientation than 
the original rectangle in order to make the door and the chimney. I called the shape classes at different sizes, 
colors, and locations to create the resulting image. I utilized the new draw methods, such as jitter, to make the image 
look as if it had been drawn by a child. 

The text files are my Lsystems. They use the various commands defined in the “drawstring” method in 
turtle interpreter to actually create the desired trees. 

