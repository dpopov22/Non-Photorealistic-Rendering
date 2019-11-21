#Domnika Popov
#Lsystem File
#10/10/19

import sys 
import random
class Lsystem:
    '''creates a new type of object, allowing new instances of that type to be made '''
     
    def __init__(self, filename = None):
        '''sets up the fields of a class and give them reasonable initial value'''
        self.base = ''
        self.rules = {}
        if filename != None:
            self.read(filename)
    
    def setBase(self, newbase):
        '''assigns the new base string to the base field of self'''
        self.base = newbase 
   
    def getBase(self): 
        '''returns the base'''
        return self.base 
    
    def getRule(self, index):
        '''returns the rule list'''
        return self.rules[index] 
    
    def addRule(self, newrule):
        '''adds a rule to the list'''
        self.rules[newrule[0]] = newrule[1:]
    
    def numRules(self):
        '''returns the length of the rule list'''
        return len(self.rules)
    
    def read(self, filename):
        '''opens the file, reads in the Lsystem information, resets the base and rules 
        fields of self, and then store the information from the file in the appropriate fields '''
        fp = open(filename,'r')
        for line in fp: 
            words = line.split()
            if words[0] == 'base': 
                self.base=words[1]
            elif words[0] == 'rule': 
                self.addRule(words[1:])
        fp.close()
        
    def replace(self, istring):
        """ Replace all characters in the istring with strings from the
            right-hand side of the appropriate rule. This version handles
            parameterized rules.
        """
        tstring = ''
        parstring = ''
        parval = None
        pargrab = False

        for c in istring:
            if c == '(':
                # put us into number-parsing-mode
                pargrab = True
                parstring = ''
                continue
            elif c == ')':
                # put us out of number-parsing-mode
                pargrab = False
                parval = float(parstring)
                continue
            elif pargrab:
                parstring += c
                continue

            if parval != None:
                key = '(x)' + c
                if key in self.rules:
                    replacement = random.choice(self.rules[key])
                    tstring += self.substitute( replacement, parval )
                else:
                    if c in self.rules:
                        replacement = random.choice(self.rules[c])
                        tstring += self.insertmod( replacement, parstring, c )
                    else:
                        tstring += '(' + parstring + ')' + c
                parval = None
            else:
                if c in self.rules:
                    tstring += random.choice(self.rules[c])
                else:
                    tstring += c

        return tstring
    
    def substitute(self, sequence, value ):
        """ given: a sequence of parameterized symbols using expressions
            of the variable x and a value for x
            substitute the value for x and evaluate the expressions
        """

        expr = ''
        exprgrab = False

        outsequence = ''

        for c in sequence:
            if c == '(':
                exprgrab = True
                expr = ''
                continue
            elif c == ')':
                exprgrab = False
                lambdafunc = eval( 'lambda x: ' + expr )
                # execute the function and put the result in a (string)
                newpar = '(' + str( lambdafunc( value ) ) + ')'
                outsequence += newpar
            # grabbing an expression
            elif exprgrab:
                expr += c
            # not grabbing an expression and not a parenthesis
            else:
                outsequence += c 

        return outsequence

    def insertmod(self, sequence, modstring, symbol):
        """ given: a sequence, a parameter string, a symbol 
            inserts the parameter, with parentheses, 
            before each
            instance of the symbol in the sequence
        """
        tstring = ''
        for c in sequence:
            if c == symbol:
                tstring += '(' + modstring + ')'
            tstring += c
        return tstring

        
    def buildString(self, iterations):
        '''makes the string'''
        nstring = self.base
        for i in range(iterations): 
            nstring = self.replace(nstring) 
        return nstring 

def main(argv):
    '''tests and runs the file'''

    if len(argv) < 2:
      print('Usage: lsystem.py <filename>')
      exit()

    filename = argv[1]
    iterations = 2

    lsys = Lsystem()

    lsys.read( filename )


    for i in range( lsys.numRules() ):
      rule = lsys.getRule(i)

    return

if __name__ == "__main__":
    main(sys.argv)
