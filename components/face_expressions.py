##################################################
# AUTHOR                                         #
# Krushna kumar V                                #
##################################################


from adafruit_servokit import ServoKit
from components.servo_worker import Servo_Worker


#Mouth full close 65
#Mouse full open 90
#left eye 97 right eye 83
#to move left eyebrow down decrease angle.
#to move right eyebrow down increase angle.
#always increase/decrease in count of  5
#eye left side 97 and right side 83

#Class to set expressions to face using servo motors
_LEFT_EYE = 7
_RIGHT_EYE = 14
_LEFT_EYE_BROW = 11
_RIGHT_EYE_BROW = 12
_MOUTH = 15

#PanTilt configuration
_PAN = 1
_TILT = 0

#Angle macro
_SMILE_LEFT_EYE = 90
_SMILE_RIGHT_EYE = 90
_SMILE_LEFT_EYE_BROW = 95
_SMILE_RIGHT_EYE_BROW = 85
_SMILE_MOUTH = 80

_SAD_LEFT_EYE = 90
_SAD_RIGHT_EYE = 83
_SAD_LEFT_EYE_BROW = 88
_SAD_RIGHT_EYE_BROW = 92
_SAD_MOUTH = 65

_ANGRY_LEFT_EYE = 90
_ANGRY_RIGHT_EYE = 97
_ANGRY_LEFT_EYE_BROW = 110
_ANGRY_RIGHT_EYE_BROW = 70
_ANGRY_MOUTH = 65

_DEFAULT_LEFT_EYE = 90
_DEFAULT_RIGHT_EYE = 90
_DEFAULT_LEFT_EYE_BROW = 98
_DEFAULT_RIGHT_EYE_BROW = 82
_DEFAULT_MOUTH = 65

#Angle for pantilt
_DEFAULT_PAN = 110
_DEFAULT_TILT = 105

_SAD_PAN = 90

class Face_Expressions:
   
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Face_Expressions, cls).__new__(cls)
        return cls.instance

  
    def __init__(self):
        self.lefteye = Servo_Worker(_LEFT_EYE)
        self.righteye = Servo_Worker(_RIGHT_EYE)
        self.mouth = Servo_Worker(_MOUTH)
        self.lefteye_brow = Servo_Worker(_LEFT_EYE_BROW)
        self.righteye_brow = Servo_Worker(_RIGHT_EYE_BROW)       
        self.pan = Servo_Worker(_PAN)
        self.tilt = Servo_Worker(_TILT)
        self.set_expression_default()
        

    def set_expression_smile(self):
        #self.lefteye.set_angle(_SMILE_LEFT_EYE)
        self.righteye.set_angle(_SMILE_RIGHT_EYE)
        self.mouth.set_angle(_SMILE_MOUTH)
        self.lefteye_brow.set_angle(_SMILE_LEFT_EYE_BROW)
        self.righteye_brow.set_angle(_SMILE_RIGHT_EYE_BROW)
        self.pan.set_angle(_DEFAULT_PAN)
            
    
    def set_expression_sad(self):
        #self.lefteye.set_angle(_SAD_LEFT_EYE)
        self.righteye.set_angle(_SAD_RIGHT_EYE)
        self.mouth.set_angle(_SAD_MOUTH)
        self.lefteye_brow.set_angle(_SAD_LEFT_EYE_BROW)
        self.righteye_brow.set_angle(_SAD_RIGHT_EYE_BROW)
        self.pan.set_angle(_SAD_PAN)
        
    def set_expression_angry(self):
        #self.lefteye.set_angle(_ANGRY_LEFT_EYE)
        self.righteye.set_angle(_ANGRY_RIGHT_EYE)
        self.mouth.set_angle(_ANGRY_MOUTH)
        self.lefteye_brow.set_angle(_ANGRY_LEFT_EYE_BROW)
        self.righteye_brow.set_angle(_ANGRY_RIGHT_EYE_BROW)
        self.pan.set_angle(_DEFAULT_PAN)

    def set_expression_default(self):
        #self.lefteye.set_angle(_DEFAULT_LEFT_EYE)
        self.righteye.set_angle(_DEFAULT_RIGHT_EYE)
        self.mouth.set_angle(_DEFAULT_MOUTH)
        self.lefteye_brow.set_angle(_DEFAULT_LEFT_EYE_BROW)
        self.righteye_brow.set_angle(_DEFAULT_RIGHT_EYE_BROW)
        self.pan.set_angle(_DEFAULT_PAN)
        self.tilt.set_angle(_DEFAULT_TILT)
    
    def set_pan_angle(self, angle): 
        if angle >= 85 and angle <= 140:
            self.pan.set_angle(angle)
            self.last_pan_angle = angle
        else:
            self.pan.set_angle(_DEFAULT_PAN)
            
           
    def set_tilt_angle(self, angle): 
        if angle >= 75 and angle <= 135:
            self.tilt.set_angle(angle)
        else:
            self.tilt.set_angle(_DEFAULT_TILT)
