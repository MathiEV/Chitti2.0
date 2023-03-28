##################################################
# AUTHOR                                         #
# GOPINATH RAJA                                  #
##################################################

from adafruit_servokit import ServoKit

from components.servo_worker import Servo_Worker
from components.face_expressions import Face_Expressions

import common.common_definitions as comm_def

_PAN = 1
_TILT = 0


#Angle for pantilt
_DEFAULT_PAN = 110
_DEFAULT_TILT = 105

_MOUTH = 15
_MOUTH_OPEN = 90
_MOUTH_CLOSE = 65

class Entertainer:

    def __init__(self, mode_monitor, gpio_worker):
        self.face_expression = Face_Expressions()
        
        self.pan = Servo_Worker(_PAN)
        self.tilt = Servo_Worker(_TILT)
        self.mouth = Servo_Worker(_MOUTH)
        
        self.__is_mouth_opened = 0
        self.__current_pan_angle = _DEFAULT_PAN
        self.__current_tilt_angle = _DEFAULT_TILT
        
        self.__mode_monitor = mode_monitor
        self.__gpio_worker = gpio_worker
        
        threading.Thread(target=self.__entertainer, daemon=True).start()
        
    def __entertainer(self):
        while True:
            if self.__mode_monitor == comm_def._FUN_MODE:
                set_mouth_open()
                
                self.face_expression.set_pan_angle(self.__current_pan_angle)
                self.face_expression.set_tilt_angle(self.__current_tilt_angle)
            else:
                set_mouth_close()
                
                
        
    def entertainer_callback(self, direction):
        if direction == comm_def._FUN_UP:
            self.__current_pan_angle = self.__current_pan_angle + 5
        elif direction == comm_def._FUN_DOWN:
            self.__current_pan_angle = self.__current_pan_angle - 5
        elif direction == comm_def._FUN_LEFT:
            self.__current_tilt_angle = self.__current_tilt_angle + 5
        elif direction == comm_def._FUN_RIGHT:
            self.__current_tilt_angle = self.__current_tilt_angle - 5
            
    
    
    def __face_up(self, pan_angle, tilt_angle ):
        self.face_expression.set_pan_angle(pan_angle)
        self.face_expression.set_tilt_angle(tilt_angle )

    def set_mouth_open(self):
        if self.__is_mouth_opened == 0:
            self.__gpio_worker.set_gpio(comm_def._LASER, True)
            self.mouth.set_angle(_MOUTH_OPEN)
            self.pan.set_angle(_DEFAULT_PAN)
            self.tilt.set_angle(_DEFAULT_TILT)
            
            self.__is_mouth_opened = 1
        
        

    def set_mouth_close(self):
        if self.__is_mouth_opened == 1:
            self.__gpio_worker.set_gpio(comm_def._LASER, False)
            self.mouth.set_angle(_MOUTH_CLOSE)
            self.pan.set_angle(_DEFAULT_PAN)
            self.tilt.set_angle(_DEFAULT_TILT)
            
            self.__is_mouth_opened = 0
        
