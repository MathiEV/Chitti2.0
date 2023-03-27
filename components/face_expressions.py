##################################################
# AUTHOR                                         #
# Krushna kumar V                                #
##################################################


from adafruit_servokit import ServoKit
from Servo_Worker import Servo_Worker

#Class to set expressions to face using servo motors
_LEFT_EYE = 1
_RIGHT_EYE = 2
_LEFT_EYE_BROW = 3
_RIGHT_EYE_BROW = 4
_MOUTH = 5

#Angle macro
_SMILE_LEFT_EYE = 0
_SMILE_RIGHT_EYE = 0
_SMILE_LEFT_EYE_BROW = 0
_SMILE_RIGHT_EYE_BROW = 0
_SMILE_MOUTH = 0

_SAD_LEFT_EYE = 0
_SAD_RIGHT_EYE = 0
_SAD_LEFT_EYE_BROW = 0
_SAD_RIGHT_EYE_BROW = 0
_SAD_MOUTH = 0

_ANGRY_LEFT_EYE = 0
_ANGRY_RIGHT_EYE = 0
_ANGRY_LEFT_EYE_BROW = 0
_ANGRY_RIGHT_EYE_BROW = 0
_ANGRY_MOUTH = 0

class Face_Expressions:
   
  
    def __init__(self):
        
        lefteye = Servo_Worker(_LEFT_EYE)
        righteye = Servo_Worker(_LEFT_EYE)
        mouth = Servo_Worker(_MOUTH)
        lefteye_brow = Servo_Worker(_LEFT_EYE_BROW)
        righteye_brow = Servo_Worker(_RIGHT_EYE_BROW)            

    def SetExpression_Happy(self):
        lefteye.setAngle(_SMILE_LEFT_EYE)
        righteye.setAngle(_SMILE_RIGHT_EYE)
        mouth.setAngle(_SMILE_LEFT_EYE_BROW)
        lefteye_brow.setAngle(_SMILE_RIGHT_EYE_BROW)
        righteye_brow.setAngle(_SMILE_MOUTH)
    
    
    def SetExpression_Sad(self):
        lefteye.setAngle(_SAD_LEFT_EYE)
        righteye.setAngle(_SAD_RIGHT_EYE)
        mouth.setAngle(_SAD_LEFT_EYE_BROW)
        lefteye_brow.setAngle(_SAD_RIGHT_EYE_BROW)
        righteye_brow.setAngle(_SAD_MOUTH)
        
     def SetExpression_Angry(self):
        lefteye.setAngle(_ANGRY_LEFT_EYE)
        righteye.setAngle(_ANGRY_RIGHT_EYE)
        mouth.setAngle(_ANGRY_LEFT_EYE_BROW)
        lefteye_brow.setAngle(_ANGRY_RIGHT_EYE_BROW)
        righteye_brow.setAngle(_ANGRY_MOUTH)
    
