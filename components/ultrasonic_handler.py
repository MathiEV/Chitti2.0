# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:02:46 2023

@author: krushnakumar
"""
import time
import threading

from ultrasonic import Ultrasonic
from application_modules.logger_module import Logger_Module

_ULTRASONIC_1_GPIO_TRIG = 16
_ULTRASONIC_2_GPIO_TRIG = 0 
_ULTRASONIC_3_GPIO_TRIG = 0

_ULTRASONIC_1_GPIO_ECHO = 12
_ULTRASONIC_2_GPIO_ECHO = 0
_ULTRASONIC_3_GPIO_ECHO = 0
    
_ULTRASONIC_SENS_DELAY = 0.1

class Ultrasonic_Handler:
    _logger = Logger_Module();
    def __init__(self):
        self.enter = True
        self.__ultrasonic1 = Ultrasonic(_ULTRASONIC_1_GPIO_TRIG, _ULTRASONIC_1_GPIO_ECHO)
        self.__ultrasonic2 = Ultrasonic(_ULTRASONIC_2_GPIO_TRIG, _ULTRASONIC_2_GPIO_ECHO)
        self.__ultrasonic3 = Ultrasonic(_ULTRASONIC_3_GPIO_TRIG, _ULTRASONIC_3_GPIO_ECHO)
      
        

    def check_for_obstacles(self):
        __center_dist = self.__ultrasonic1.get_distance_in_cm()
        __left_dist = self.__ultrasonic2.get_distance_in_cm()
        __right_dist = self.__ultrasonic3.get_distance_in_cm()
        
        self._logger.logDebug(__center_dist, __left_dist, __right_dist)
        object_details = {}
        object_details[0] = __right_dist
        object_details[1] = __center_dist       
        object_details[2] = __left_dist
        
        time.sleep(_ULTRASONIC_SENS_DELAY)

        self._logger.logDebug(object_details[0], object_details[0], object_details[0])

        return object_details
        
    def stop(self):
        # Reset GPIO Pins.  
        self.__ultrasonic1.clean_GPIO_pins()
        self.__ultrasonic2.clean_GPIO_pins()
        self.__ultrasonic3.clean_GPIO_pins()
        
        

    
