# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:02:46 2023

@author: krushnakumar
"""
import time
import threading

from ultrasonic import Ultrasonic

_ULTRASONIC_1_GPIO_TRIG = 16
_ULTRASONIC_2_GPIO_TRIG = 0 
_ULTRASONIC_3_GPIO_TRIG = 0

_ULTRASONIC_1_GPIO_ECHO = 12
_ULTRASONIC_2_GPIO_ECHO = 0
_ULTRASONIC_3_GPIO_ECHO = 0
     
_ULTRASONIC_THRESHOLD_DIST = 30 #distance in cms
_ULTRASONIC_SENS_DELAY = 0.1

class Ultrasonic_Handler:
    def __init__(self):
        self.enter = True
        self.__ultrasonic1 = Ultrasonic(_ULTRASONIC_1_GPIO_TRIG, _ULTRASONIC_1_GPIO_ECHO)
        self.__ultrasonic2 = Ultrasonic(_ULTRASONIC_2_GPIO_TRIG, _ULTRASONIC_2_GPIO_ECHO)
        self.__ultrasonic3 = Ultrasonic(_ULTRASONIC_3_GPIO_TRIG, _ULTRASONIC_3_GPIO_ECHO)
        #Creating thread
        threading.Thread(target=self.___Check_for_Obstacles, daemon=True).start()

    def ___Check_for_Obstacles(self):
        object_details = {}

        while(self.enter):
            __center_dist = self.__ultrasonic1.get_distance_in_cm()
            __left_dist = self.__ultrasonic2.get_distance_in_cm()
            __right_dist = self.__ultrasonic3.get_distance_in_cm()
            
            print(__center_dist, __left_dist, __right_dist)
            
            if (__center_dist <= _ULTRASONIC_THRESHOLD_DIST):

                object_details[0] = 0
            else:
                object_details[0] = 1
            
            if (__left_dist <= _ULTRASONIC_THRESHOLD_DIST):
                object_details[1] = 0
            else:
                object_details[1] = 1
                
            if (__right_dist <= _ULTRASONIC_THRESHOLD_DIST):
                object_details[2] = 0
            else:
                object_details[2] = 1
            
            time.sleep(_ULTRASONIC_SENS_DELAY)

            print(object_details[0], object_details[0], object_details[0])

            return object_details
        
    def stop(self):
        self.enter = False
        time.sleep(1)
        # Reset GPIO Pins.  
        self.__ultrasonic1.clean_GPIO_pins()
        self.__ultrasonic2.clean_GPIO_pins()
        self.__ultrasonic3.clean_GPIO_pins()
        
        

    
