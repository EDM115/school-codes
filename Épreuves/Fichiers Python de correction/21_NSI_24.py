class AdresseIP:

    def __init__(self, adresse):
        self.adresse = ...

    def liste_octet(self):
        """renvoie une liste de nombres entiers,
           la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")] 

    @staticmethod
    def est_reservee():
        """renvoie True si l'adresse IP est une adresse
           réservée, False sinon"""
        return ... or ...

    @staticmethod
    def adresse_suivante():
        """renvoie un objet de AdresseIP avec l'adresse 
           IP qui suit l’adresse self
           si elle existe et False sinon"""
        if ... < 254:
            octet_nouveau = ... + ...
            return AdresseIP('192.168.0.' + ...)
        return False
