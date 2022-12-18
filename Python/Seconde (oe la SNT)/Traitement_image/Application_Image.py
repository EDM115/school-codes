from  javax.imageio import ImageIO
from  java.io import File,IOException
from java.awt.image import BufferedImage
from java.awt import Color,BorderLayout,GridLayout,Dimension,Insets
from javax.swing import JFrame,JPanel,JButton,JLabel,ImageIcon,Icon
# initialisation des variables globales
#*********** PARTIE 1  *********** PARTIE 1  *********** PARTIE 1  *********** PARTIE 1 ***********
msg=["miroirH","permuteRB"]
filename="falaise.png"
dimX=5 # dimension du tableau des boutons
dimY=2
#*********** FIN PARTIE 1  *********** FIN PARTIE 1  *********** FIN PARTIE 1  *********** FIN PARTIE 1 ***********

#*********** PARTIE 2  *********** PARTIE 2  *********** PARTIE 2  *********** PARTIE 2***********
# gestion des différents traitement de l'image  
def traitement(i):
  global imgF
  i=int(i)
  if i==0:
    miroirH() 
  elif i==1:
    permuteRB()
# associer le n° du bouton à son traitement








#*********** FIN PARTIE 2  *********** FIN PARTIE 2 *********** FIN PARTIE 2  *********** FIN PARTIE 2 ***********

# ne pas mofifier la ligne suivante 
  labelImage.setIcon(ImageIcon(imgF))

#********************************************* Les différents traitements ***************************************  



#*********** PARTIE 3  *********** PARTIE 3  *********** PARTIE 3  *********** PARTIE 3***********
def miroirH():
  global imgO,imgF,largeur,hauteur 
  imgF=BufferedImage(largeur,hauteur,BufferedImage.TYPE_INT_RGB)#déclaration des dimensions de l'image résultat et du type de codage de la couleur

  for i in range(largeur):
   for j in range (hauteur):
      rgb=imgO.getRGB(largeur-1-i, j)
      imgF.setRGB(i,j,rgb)

def permuteRB():
  global imgO,imgF,largeur,hauteur 
  imgF=BufferedImage(largeur,hauteur,BufferedImage.TYPE_INT_RGB)#déclaration des dimensions de l'image résultat et du type de codage de la couleur

  for i in range(largeur):
   for j in range (hauteur):
      rgb=imgO.getRGB(i, j)# récupération du code rgb du pixel (i,j)
      r=getRed(rgb)# récupération de la composante rouge du pixel (i,j)
      g=getGreen(rgb)# récupération de la composante verte du pixel (i,j)
      b=getBlue(rgb)# récupération de la composante bleue du pixel (i,j)
      imgF.setRGB(i,j,makeRGB(b,g,r)) # le pixel(i,j) prend la couleur créée avec makeRGB

#************************************************ Insérer ici vos différents traitements ***************************************************************









#*********** FIN PARTIE 3  *********** FIN PARTIE 3 *********** FIN PARTIE 3  *********** FIN PARTIE 3 ***********

#************************************************************************************************************
#***************** Attention ne rien modifier dans les lignes suivantes *************************************  
def makeRGB(r,g,b):
    return (r<<16)+(g<<8)+b

def getRed(rgb):
    return(rgb>>(16))&0xFF

def getGreen(rgb):
    return(rgb>>(8))&0xFF

def getBlue(rgb):
    return rgb&0xFF

def initialisation():
    global imgO,labelImage,frameWidth,frameHeight,b,largeur,hauteur
    frameWidth=1020
    frameHeight=800
    f=JFrame(title="Traitement de l'image",size=(frameWidth,frameHeight))
    f.contentPane.layout=BorderLayout()
    initBouton()
    f.contentPane.add(b,BorderLayout.SOUTH)
    imgO=readImage(filename)
    largeur=imgO.getWidth()
    hauteur=imgO.getHeight()
    labelImage = JLabel(ImageIcon(imgO))
    labelImage_ = JLabel(ImageIcon(imgO))
    f.contentPane.add(labelImage_,BorderLayout.WEST)
    f.contentPane.add(labelImage,BorderLayout.EAST)
    f.setVisible(True)

def readImage(filename): # fonction de lecture d'une image dont le nom est Filename. Cette retourne un objet de type Image
    global imgO
    e=None
    image_=None
    try:
        path=File(filename).getAbsolutePath()
        print(File(filename).getAbsolutePath())
        image_= ImageIO.read(File(path))# Le fichier file est interprété comme étant une image que l'on nomme image
        """print(File(filename).getAbsolutePath())
        image_= ImageIO.read(File(filename))# Le fichier file est interprété comme étant une image que l'on nomme image
        """
    except IOException(e):
        print (e)
    return image_

# initialisation du tableau des boutons        
def initBouton(): 
  global b,dimX,dimY
  b=JPanel()
  cmd=[[None]*dimX for i in range(dimY)]
  b.layout=GridLayout(dimY,dimX)
  for i in range(dimY):
      for j in range(dimX):
          k=i*dimX+j
          if (k<len(msg)):
            message=msg[k]# msg.length taille du tableau msg
          else:
            message=""
          bouton =JButton(message, actionPerformed = action)# déclaration d'un bouton où est inscrit le texte message et son action
          bouton.setName(""+str(k))# nom du bouton pour faciliter le repérage du bouton actionné
          bouton.setPreferredSize(Dimension(100,50))# taille des boutons (largeur, hauteur)
          bouton.setFont(bouton.getFont().deriveFont(float(14)))# taille du texte
          bouton.setBackground(Color.WHITE)# couleur du bouton
          bouton.setForeground(Color.RED)# couleur du texte
          bouton.setMargin(Insets(0,0,0,0))#
          b.add(bouton)#insertion du bouton dans le panneau des boutons

      if j==dimX: j=dimX-1
      cmd[i][j]= bouton

# Récupération du n° du bouton actif pour appliquer le traitement correspondant
def action(event):
    i=event.getSource().getName()
    traitement(i)

# lancement du programme    
initialisation()
