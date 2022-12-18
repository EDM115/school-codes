#!/usr/bin/env python
# -*- coding: latin-1 -*-
class Tableau:
    #type_= int, bool, float, str, char
    Type={'int':'int','i':'int'}

    def __init__(self,type_,taille):
        pass  

    def getTypeStr(self):
        print( "<type 'array of "+str(self.n)+" "+self.type_+"'>")

    def getType(self):
        pass  


    def getLen(self): 
        pass

    def setElement(self,i,e):
        pass

    def getElement(self,i):
        pass




class IndexError(Exception):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    """def __init__(self, message):
        #self.expression = expression
        if message==None:
            message="ArrayBound Exception"
        self.message = message
        """

t=T('int',5)
t.setElement(0,1)
print(t.getElement(4))
print(t.getLen())
print(t.getType())
