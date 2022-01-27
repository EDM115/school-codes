class Voiture:
    def __init__ (self, couleur, kilometrage, type_carburant, nb_roues):
        self.__couleur = couleur
        self.__kilometrage = kilometrage
        self.__type_carburant = type_carburant
        self.__nb_roues = nb_roues
    def peindre(self, nouvelle_couleur):
        self.__couleur = nouvelle_couleur
    def rouler(self, distance):
        self.__kilometrage += distance

    def get_couleur(self):
        return self.__couleur
    def get_kilometrage(self):
        return self.__kilometrage
    def get_type_carburant(self):
        return self.__type_carburant
    def get_nb_roues(self):
        return self.__nb_roues

ferrari = Voiture("rouge", 10000, "essence", 4)
ferrari.peindre("jaune")
ferrari.rouler(500)
print("La couleur de ma Ferrari est " + ferrari.get_couleur() + ", elle a roulé " + str(ferrari.get_kilometrage()) + " km, utilise le carburant " + ferrari.get_type_carburant() +  " et possède " + str(ferrari.get_nb_roues()) + " roues.")