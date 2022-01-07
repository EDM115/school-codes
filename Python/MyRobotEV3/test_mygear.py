from ev3robot import *
from mygear import MyGear

robot = LegoRobot()
gear = MyGear()
robot.addPart(gear)
robot.drawString('test',0,0)

gear.setSpeed(50)
gear.forward_(50.0)
gear.left_(90.0)
gear.forward_(50.0)
gear.leftArc_(0.25,180.0)
gear.rightArc_(0.25,180.0)
gear.backward_(50.0)
robot.exit()    