class Cercle :
    def __init__(self, couleur, rayon, x, y):
        self.__couleur=couleur
        self.__rayon=rayon
        self.__x=x
        self.__y=y
    def set_x(self, x):
        self.__x=x
    def set_y(self, y):
        self.__y=y
    def set_attribut(self, **kwargs):
        for key in kwargs:
            if key=='couleur':
                self.set_couleur(kwargs[key])
            elif key=='rayon':
                self.set_rayon(kwargs[key])
            elif key=='x':
                self.set_x(kwargs[key])
            elif key=='y':
                self.set_y(kwargs[key])

C1=Cercle('blue', 10, 1, 0)
