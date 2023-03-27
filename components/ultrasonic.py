# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 15:53:42 2023

@author: krushnakumar
reference https://www.bluetin.io/sensors/python-library-ultrasonic-hc-sr04/
"""
import RPi.GPIO as GPIO
from Bluetin_Echo import Echo  

_SPEED_OF_SOUND = 340
_NO_OF_SAMPLES = 5

class Ultrasonic:
    def __init__(self, trigger_pin, echo_pin):
        # Define GPIO pin constants.  
        self.__trigger_pin = trigger_pin  
        self.__echo_pin = echo_pin 
        # Initialise Sensor with pins, speed of sound.  
        self.speed_of_sound = _SPEED_OF_SOUND 
        self.echo = Echo(self.__trigger_pin, self.__echo_pin, self.speed_of_sound)  

    def get_distance_in_cm(self):
        __distance = self.echo.read('cm', _NO_OF_SAMPLES)  	
        return __distance    
        
    def clean_GPIO_pins(self):
        # Reset GPIO Pins.  
        self.echo.stop()

    
