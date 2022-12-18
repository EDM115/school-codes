class Arbre:
	def __init__(self,valeur):
		self.noeud = valeur
		self.fils = []

	def insere_fils(self,arbre):
		self.fils.append(arbre)

	def insere_noeud(self, valeur):
		self.fils.append(Arbre(valeur))

	def taille(self):
		n = 1
		for fils in self.fils:
			n = n + fils.taille()
		return n

	def hauteur(self):
		hmax = 1
		if len(self.fils) != 0:
			for fils in self.fils:
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
		pass

	def prefixe(self,parcours):
		parcours.append(self.noeud)
		for fils in self.fils:
			fils.prefixe(parcours)

	def postfixe(self,parcours):
		pass

	def largeur(self):
		pass

	def affiche(self,d):
		"""Fonction recursive qui renvoie l'arbre sous forme de chaine de caracteres"""
		e=len(str(self.noeud))
		if len(self.fils)==0: # le noeud est une feuille
			return'-['+str(self.noeud)+']'
		s='-['+str(self.noeud)+']'
		d_=d
		a=''
		for e_ in range(e+3): # decalage pour que les noeuds de meme niveau soient alignes
					a=a+' '
		if len(self.fils)>1:
			d=d+a+chr(124)
		else:
			d=d+a+' ' #traitement particulier du 1er fils
		s=s+'-'+self.fils[0].affiche(d)+'\n'
		for i in range(1,len(self.fils)-1): # traitement des autres fils
				s=s+d+self.fils[i].affiche(d)+'\n'
		if len(self.fils)>1: # traitement particulier du dernier fils
			s=s+d+self.fils[-1].affiche(d_+a+' ')+'\n'
		s=s+d[:-1]
		return s

	def __repr__(self):
		"""
		Fonction qui nettoie la chaine de caracteres construite par la fonction recursive printTree_ et dessine l'arbre.
		Pour l'affichage, faire print(arbre) ou arbre est une instance de la classe Arbre
		"""
		s=self.affiche('')
		a=s.split('\n') # on decoupe la chaine de caracteres aux niveaux des retours a la ligne \n
		i=0
		while i <len(a):
			j=len(a[i])-1
			while j >=0 and a[i][j]==' ': #suppression des espaces surnuneraires
				if a[i][j]==' ':
					a[i]=a[i][:-1]
				j=len(a[i])-1
			i=i+1
		i=0
		while i <len(a)-1: #suppression des lignes identiques
			if a[i]==a[i+1]:
				del a[i]
			else:
				i=i+1
		s=''
		for i, item in enumerate(a):
			s=s+item+'\n'
		return s

a=Arbre(1)
a.insere_noeud(2)
a.insere_noeud(3)
a.insere_noeud(4)
a.fils[0].insere_noeud(5)
a.fils[0].insere_noeud(6)
a.fils[1].insere_noeud(7)
a.fils[1].insere_noeud(8)
a.fils[1].insere_noeud(9)
a.fils[1].insere_noeud(10)
a.fils[1].fils[1].insere_noeud(11)
a.fils[1].fils[1].insere_noeud(12)
print(a)
print("hauteur",a.hauteur())
print("taille",a.taille())
print("nb de feuilles",a.nb_feuilles())
print("arité",a.arite())
parcours=[]
a.prefixe(parcours)
print("parcours préfixe",parcours)
parcours=[]
a.postfixe(parcours)
print("parcours postfixe",parcours)
print("parcours largeur",a.largeur())
