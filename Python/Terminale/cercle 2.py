from tkinter import *
root = Tk()
myCanvas = Canvas(root)
myCanvas.pack()
class Cercle:
    def __init__(self,couleur,rayon,x,y):
        self.__couleur=couleur
        self.__rayon=rayon
        self.__x=x
        self.__y=y



    def get_rayon(self):
        return self.__rayon
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_couleur(self):
        return self.__couleur

    def delete(self):
        pass
C1=Cercle('red',10,5,5)
print(C1.get_x())



def draw(canvasName): #center coordinates, radius
    x1= C1.get_x() + C1.get_rayon()
    y1 = C1.get_y() + C1.get_rayon()
    return canvasName.create_oval(x1, y1)

draw(100, 100, 20, myCanvas)
draw(50, 25, 10, myCanvas)
root.mainloop()
