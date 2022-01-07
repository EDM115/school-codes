
from simrobot import *
#from ev3robot import *
from mygearsim import MyGear

RobotContext.setStartPosition(250,250)            
robot = LegoRobot()
robot.drawString("toto",0,0)
gear = MyGear()
robot.addPart(gear)
gear.forward_(50.0)
gear.left_(90.0)
gear.forward_(50.0)
gear.leftArc_(0.25,180.0)
gear.rightArc_(0.25,180.0)
gear.backward_(50.0)
robot.exit()
