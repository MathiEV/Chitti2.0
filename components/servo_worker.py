##################################################
# AUTHOR                                         #
# Sathya Bama Plaanisamy                         #
##################################################
from adafruit_servokit import ServoKit

class Servo_Worker:
   
    #ZeroOffset is the intial value/position required for the servo motor
    
    _kit = ServoKit(channels=16)
    _kit.frequency = 60
    _actuationRange = 180

    def __init__(self, input_channel):
        print("Servo worker init started")
        self.channel = input_channel            
        self._kit.servo[self.channel].actuation_range = self._actuationRange
        #Modify the pulse width range based on the servo
        self._kit.servo[self.channel].set_pulse_width_range(0, 2520)
        print("Servo worker init completed")

    def setAngle(self, angle):
        self._kit.servo[self.channel].angle = angle
