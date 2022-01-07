from ev3robot import *
DEFAULT_GEAR_SPEED = 30
DEFAULT_STEP_FACTOR=25000/11 #temps*50 pour se déplacer d'un pixel à une vitesse de 50
DEFAULT_RADIUS_FACTOR=5000 # Coefficient de correction du rayon pour leftArc et rightArc 
DEFAULT_ROTATION_FACTOR = 10800/53 #temps*10 pour un degré à la vitesse de 10
DEFAULT_SPEED_ROTATION_FACTOR=0.2 # pour la rotation par défaut 20% de la vitesse lineaire

class MyGear(Gear):
    def init(self):
        self.stepFactor=DEFAULT_STEP_FACTOR
        self.rotationFactor=DEFAULT_ROTATION_FACTOR 
        self.radiusFactor=DEFAULT_RADIUS_FACTOR
        self.speedRotationFactor=DEFAULT_SPEED_ROTATION_FACTOR
        self.speed=DEFAULT_GEAR_SPEED 
        
    def setRotationFactor(self,anglefactor): 
        self.rotationFactor=anglefactor*DEFAULT_ROTATION_FACTOR 
        
    def setStepFactor(self,stepfactor): 
        self.stepFactor=stepfactor*DEFAULT_STEP_FACTOR 
        
    def setSpeedRotationFactor(self,speedRotationFactor): 
        self.speedRotationFactor=speedRotationFactor
        
    def setRadiusFactor(self,radiusfactor): 
        self.radiusFactor=radiusfactor*DEFAULT_RADIUS_FACTOR     
             
    def left_(self,*args):    
        if self.speed == 0:
            return
        if (len(args)==0):
            self.left()
        elif (type(args[0])==int):
            if (args[0]>0):
                self.left(args[0])
            else:
                self.right(-args[0])
        else:                    
            speed_ = self.speed
            rotationspeed=self.speed*self.speedRotationFactor
            if ( rotationspeed>100):
                 self.setSpeed(100)
            elif (rotationspeed<10):
                self.setSpeed(10)
            else: 
                self.setSpeed(int(rotationspeed))
            angle=int(round(args[0]*self.rotationFactor/self.speed))
            self.left(angle)
            self.setSpeed(speed_) 

    def right_(self,*args):
        if self.speed == 0:
           return
        if (len(args)==0):
            self.right()
        elif (type(args[0])==int):
            if (args[0]>0):
                self.right(args[0])
            else:
                self.left(-args[0])
        else:                    
            speed_ = self.speed           
            rotationspeed=self.speed*self.speedRotationFactor
            if ( rotationspeed>100):
                 self.setSpeed(100)
            elif (rotationspeed<10):
                self.setSpeed(10)
            else: 
                self.setSpeed(int(rotationspeed))
            angle=int(round(args[0]*self.rotationFactor/self.speed))
            self.right(angle)
            self.setSpeed(speed_) 
            
    def forward_(self,*args):
         if self.speed == 0:
             return
         if (len(args)==0):
            self.forward()
         elif (type(args[0])==int):
            if (args[0]>0):
                self.forward(args[0])
            else:
                self.backward(-args[0])
         else:
            if (args[0]>0):
                self.forward(int(round(self.stepFactor * args[0]/self.speed))) 

    def backward_(self,*args):
         if self.speed == 0:
             return
         if (len(args)==0):
            self.backward()
         elif (type(args[0])==int):
            if (args[0]>0):
                self.backward(args[0])
            else:
                self.forward(-args[0])
         else:
            if (args[0]>0):
                self.backward(int(round(self.stepFactor * args[0]/self.speed)))             
                            
    def leftArc_(self, *args):
        if self.speed == 0:
            return
        radius = args[0]
        if (len(args)==1):
                self.leftArc(radius)
        elif(type(args[1])==int):  
            if (args[1]>0):
                self.leftArc(args[0],args[1])
            else:
                self.rightArc(radius,-args[1])
        else:
            angle=int(round(radius*self.radiusFactor*args[1]/self.speed))
            if (args[1]>0):
                self.leftArc(radius,angle)
            else:
                self.rightArc(radius,-angle)
                
    def rightArc_(self, *args):
        if self.speed == 0:
            return
        radius = args[0]
        if (len(args)==1):
                self.rightArc(radius)
        elif(type(args[1])==int):  
            if (args[1]>0):
                self.rightArc(args[0],args[1])
            else:
                self.left(radius,-args[1])
        else:
            angle=int(round(radius*self.radiusFactor*args[1]/self.speed))
            if (args[1]>0):
                self.rightArc(radius,angle)
            else:
                self.leftArc(radius,-angle)
                                 
#    def getSpeed(self):
#        return self.speed
