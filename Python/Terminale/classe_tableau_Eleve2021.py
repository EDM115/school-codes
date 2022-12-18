#!/usr/bin/env python
# -*- coding: latin-1 -*-
class Tableau:
    #type_= int, bool, float, str, char
    Type={'int':int, 'i':int, 'bool':bool, 'b':bool}
    
    def __init__(self,type_,taille):
        if type_ in Tableau.Type:
            self.__type = Tableau.Type[type_]
            self.__tab = [None]*5
            self.__tab
        else:
            print("type non reconnu")
    
    def getTypeStr(self):
        print("<type 'array of " + str(self.n) + " " + self.type_ + "'>")
    
    def getType(self):
        return self.__type
    
    def getLen(self):
        return len(self.__tab)
    
    '''def setElement(self,i,e):
        print(type(e), "<type '"+str(self.__type)+"'>")
        if str(type(e))=="<type '"+str(self.__type)+"'>":
            if isinstance(e, self.__type):
                if -1<i and i<self.getLen():
                    self.__tab[i]=e
                else:
                    print("index out of range")
        else:
            print("erreur de type")'''

    def setElement(self, i, elt):
        if (isinstance(elt, self.__type)) and (i >= 0 and i < self.__taille):
            self.__tab[i] = elt

    def __setItem__(self, i, elt):
        self.setElement(i, elt)
    
    def getElement(self,i):
        if i > 0 and i < self.__taille:
            return self.__taille[i]
    
    def __getItem__(self, i):
        return self.getElement(i)

class IndexError(Exception):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    pass
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
