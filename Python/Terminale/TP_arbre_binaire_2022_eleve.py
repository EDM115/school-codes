class Arbre:
	def __init__(self,valeur):
		self.noeud = valeur
		self.fils_gauche = None
		self.fils_droit = None
		
	def insere_fils_droit(self,fils):
		self.fils_droit = fils
		
	def insere_fils_gauche(self,fils):
		self.fils_gauche = fils
		
	def insere_noeud_droit(self, valeur):
		self.fils_droit = Arbre(valeur)
		
	def insere_noeud_gauche(self, valeur):
		self.fils_gauche = Arbre(valeur)
	
	def taille(self):
		n = 1
		for fils in self.fils:
			n = n + fils.taille()
		return n 
		
	def hauteur(self):
		hmax = 1
		if len(self.fils_gauche) != 0:
			for fils in self.fils_gauche:
				h = fils.hauteur()
				if h > hmax:
					hmax = h
			hmax = hmax + 1
		return hmax
	
	def nb_feuilles(self):
		if len(self.fils) == 0:
			n = 1
		else:
			n = 0
			for fils in self.fils:
				n = n + fils.nb_feuilles()
		return n
	
	def arite(self):
		nmax = 0
		# à compléter 
		return nmax
	
	def largeur(self):
		arbres = [self]
		parcours = []
		while arbres != []:
			arbre = arbres.pop(0)
			# à compléter 
			parcours.append(arbre.noeud)
		return parcours
	
	def prefixe(self,parcours):
		pass

	def postfixe(self,parcours):
		pass
	
	def infixe(self,parcours):
		pass
		
	def recherche(self, x):
		trouvé = False
		if self.noeud is not None:
			if x == self.noeud:
				trouvé = True
			else:
				if x < self.noeud:
					trouvé = self.fils_gauche.recherche(x)
				else:
					trouvé = self.fils_droit.recherche(x)
		return trouvé
	
	def ajouter(self, x):
		if self.noeud is not None:
			if x < self.noeud:
				if self.fils_gauche is not None:
					self.ajouter(x, self.fils_gauche)
				else:
					self.insere_fils_gauche(x)
			else:
				if self.fils_droit is not None:
					self.ajouter(x, self.fils_droit)
				else:
					self.insere_fils_droit(x)
		else:
			self.noeud = x

	def suppr_via_max(self, x):
		if x < self.noeud:
			self.suppr_via_max(self.fils_gauche, x)
		else:
			if x > self.noeud:
				self.suppr_via_max(self.fils_droit, x)
			else:
				if x == self.noeud:
					if self.fils_droit is not None:
						self.noeud = self.noeud.fils_droit
						self.suppr_via_max(self.noeud, self.noeud.fils_droit)
					else:
						if self.fils_gauche is not None:
							self.noeud = self.noeud.fils_gauche
							self.suppr_via_max(self.noeud, self.noeud.fils_gauche)
						else:
							self.noeud.fils_droit = None

	def doublon(self):
		trouve = False
		if self.fils_gauche is not None:
			trouve = self.recherche(self.fils_gauche, self.noeud)
			if trouve is False:
				trouve = self.doublon(self.fils_gauche, self.noeud)
		if trouve is False:
			if self.fils_droit is not None:
				trouve = self.doublon(self.fils_droit)
		return trouve

	def doublon_qui_marche(self, x):
		trouve2 = False
		if self.fils_gauche is not None:
			trouve2 = self.fils_gauche.recherche(x)
			if trouve2 is False:
				trouve2 = self.fils_gauche.doublon_qui_marche(self.fils_gauche.noeud)
		if trouve2 is False:
			if self.fils_droit is not None:
				trouve2 = self.fils_droit.doublon_qui_marche(self.fils_droit.noeud)
		return trouve2

	def suppr2(self, x, a):
		if self.noeud == x:
			if self.fils_gauche is None:
				if self.fils_droit is None:
					self.noeud = self.fils_droit.noeud
					self.fils_gauche = self.fils_droit.fils_gauche
					self.fils_droit = self.fils_droit.fils_droit
				else:
					if a.self.fils_droit == self:
						a.self.fils_droit = None
					else:
						a.self.fils_gauche = None
			else:
				if self.fils_droit is None:
					self.noeud = self.fils_gauche.fils_noeud
					self.fils_gauche = self.fils_gauche.fils_gauche
					self.fils_droit = self.fils_gauche.fils_droit
				else:
					m = self.droit.min()
					self.noeud = m
					self.fils_droit.suppr2(m.self)
		elif self.noeud > x:
			if self.fils_gauche is not None:
				self.fils_gauche.suppr2(x, self)
		else:
			if self.fils_droit is not None:
				self.fils_droit.suppr2(x, self)

	def supprime(self, x):
		self.suppr2(x, None)

a.insere_noeud_gauche(10) 
a.insere_noeud_droit(40)
a.fils_gauche.insere_noeud_gauche(4)
a.fils_droit.insere_noeud_gauche(32)
a.fils_droit.insere_noeud_droit(45)
a.fils_gauche.fils_gauche.insere_noeud_droit(7)
a.fils_droit.fils_gauche.insere_noeud_droit(38)
a.fils_droit.fils_gauche.fils_droit.insere_noeud_gauche(33)
a.fils_droit.fils_gauche.fils_droit.insere_noeud_droit(39)

print(a)
print("hauteur",a.hauteur())   
print("taille",a.taille())
print("arite",a.arite())
print("nb de feuilles",a.nb_feuilles()) 
parcours=[]
a.prefixe(parcours)
print("parcours préfixe",parcours) 
parcours=[]
a.postfixe(parcours) 
print("parcours postfixe",parcours)
parcours=[]
a.infixe(parcours) 
print("parcours infixe",parcours)
print("parcours largeur",a.largeur())
print(a.recherche(32))
print(a.doublon)