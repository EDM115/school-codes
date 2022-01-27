class Cercle :
    def __init__ (self, couleur, rayon, x, y):
        self.__couleur=couleur
        self.__rayon= rayon
        self.__x=x
        self.__y=y

    def set_x (self, x):
        self.__x=x

    def set_y (self, y):
        self.__y=y

    def couleur (self, couleur):
        self.__couleur=couleur

    def rayon (self, rayon):
        self.__rayon=rayon

    def get_x (self):
        return self.__x

    def get_y (self):
        return self.__y

    def get_couleur (self):
        return self.__couleur

    def get_rayon (self) :
        return self.__rayon

    def set_attribut (self, **kwrgs):
        for key in kwargs:
            if key == 'couleur':
                self.set_couleur(kwargs [key])
            elif key == 'rayon':
                self.set_rayon(kwargs [key])
            elif key == 'x':
                self.set_x(kwargs [key])
            elif key == 'y':
                self.set_y(kwargs [key])


r1=c1.get_rayon
r2=c2.get_rayon


distance=sqrt((c1.get_x-c2.get_x)**2+(c1.get_y-c2.get_y)**2)

    def intersection (distance, r1, r2):
        if distance>=r1+r2 and distance+min>=max :


c1=Cercle('red', 100, 0, 0)
print(c1.get_rayon())
print(c1.get_couleur())


c2=Cercle('blue', 50, 10, 5)
print(c2.get_rayon())
print(c2.get_couleur())