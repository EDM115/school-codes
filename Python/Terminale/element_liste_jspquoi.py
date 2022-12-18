class Element:
    def __init__(self, car_, cdr_):
        self.car = car_
        self.cdr = cdr_

class Liste:
    def __init__(self):
        self.elt = None
    
    def estVide(self):
        return self.elt is None
    
    def car(self):
        if self.estVide():
            return None
        return self.elt.car
    
    def cdr(self):
        if self.estVide():
            return None
        return self.elt.cdr
    
    def cons(self, element, liste):
        if element is not None:
            element.cdr = Liste
            return Liste(element)
    
    def afficher(self):
        element = self.elt
        while element is not None:
            if element.cdr is not None:
                element = element.cdr.elt
            else:
                element = None

L0 = Liste(Element(5,None))
L1 = L0.cons(Element(8, None), L0)
L2 = L1.cons(Element(-4, None), L1)
L2.afficher()