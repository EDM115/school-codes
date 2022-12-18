from random import *

class Combattant:

    def __init__(self,vie,force,nom):
        self.__vie = vie
        self.__force = force
        self.__nom = nom

    def get_vie(self):
        return self.__vie

    def get_force(self):
        return self.__force

    def get_nom(self):
        return self.__nom

    def set_vie(self,vie):
        self.__vie = vie

    def set_force(self,force):
        self.__force = force


GURU = Combattant(10,15,'GURU')
BUlly = Combattant(10,15,'BUlly')

def score():
    print('La vie de GURU est de  ' + str(GURU.get_vie()))
    print('La vie de BUlly est de ' + str(BUlly.get_vie()))
def attaquer():
    GURU.set_force(randint(0,10))
    BUlly.set_force(randint(0,10))
    if GURU.get_force()>BUlly.get_force():
        BUlly.set_vie(BUlly.get_vie()-1)
        score()
    elif GURU.get_force()<BUlly.get_force():
        GURU.set_vie(GURU.get_vie()-1)
        score()
    else:
        print('égalité')
    print('')

while GURU.get_vie()>0 or BUlly.get_vie()>0:
    attaquer()
    if GURU.get_vie()==0:
        print ("fin du combat, BUlly gagne")
        break
    elif BUlly.get_vie()==0:
        print ("fin du combat, GURU gagne")
        break
