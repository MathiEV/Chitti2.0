##################################################
# AUTHOR                                         #
# Krushna kumar V                                #
##################################################


from adafruit_servokit import ServoKit
from components.servo_worker import Servo_Worker

#Class to set expressions to face using servo motors
_LEFT_EYE = 1
_RIGHT_EYE = 2
_LEFT_EYE_BROW = 3
_RIGHT_EYE_BROW = 4
_MOUTH = 5

#Angle macro
_SMILE_LEFT_EYE = 90
_SMILE_RIGHT_EYE = 90
_SMILE_LEFT_EYE_BROW = 90
_SMILE_RIGHT_EYE_BROW = 90
_SMILE_MOUTH = 90

_SAD_LEFT_EYE = 90
_SAD_RIGHT_EYE = 90
_SAD_LEFT_EYE_BROW = 90
_SAD_RIGHT_EYE_BROW = 90
_SAD_MOUTH = 90

_ANGRY_LEFT_EYE = 90
_ANGRY_RIGHT_EYE = 90
_ANGRY_LEFT_EYE_BROW = 90
_ANGRY_RIGHT_EYE_BROW = 90
_ANGRY_MOUTH = 90

class Face_Expressions:
   
  
    def __init__(self):
        self.lefteye = Servo_Worker(_LEFT_EYE)
        self.righteye = Servo_Worker(_LEFT_EYE)
        self.mouth = Servo_Worker(_MOUTH)
        self.lefteye_brow = Servo_Worker(_LEFT_EYE_BROW)
        self.righteye_brow = Servo_Worker(_RIGHT_EYE_BROW)            

    def SetExpression_Happy(self):
        self.lefteye.set_angle(_SMILE_LEFT_EYE)
        self.righteye.set_angle(_SMILE_RIGHT_EYE)
        self.mouth.set_angle(_SMILE_LEFT_EYE_BROW)
        self.lefteye_brow.set_angle(_SMILE_RIGHT_EYE_BROW)
        self.righteye_brow.set_angle(_SMILE_MOUTH)
    
    
    def SetExpression_Sad(self):
        self.lefteye.set_angle(_SAD_LEFT_EYE)
        self.righteye.set_angle(_SAD_RIGHT_EYE)
        self.mouth.set_angle(_SAD_LEFT_EYE_BROW)
        self.lefteye_brow.set_angle(_SAD_RIGHT_EYE_BROW)
        self.righteye_brow.set_angle(_SAD_MOUTH)
        
    def SetExpression_Angry(self):
        self.lefteye.set_angle(_ANGRY_LEFT_EYE)
        self.righteye.set_angle(_ANGRY_RIGHT_EYE)
        self.mouth.set_angle(_ANGRY_LEFT_EYE_BROW)
        self.lefteye_brow.set_angle(_ANGRY_RIGHT_EYE_BROW)
        self.righteye_brow.set_angle(_ANGRY_MOUTH)
    
