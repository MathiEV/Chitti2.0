# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 19:00:05 2023

AUTHOR                                         
Krushna kumar V                                
"""
import time

from component.gpio_worker import GPIO_Worker

#Motor1 right
_MOTOR1_IN1_ = 0 
_MOTOR1_IN2_ = 0
_MOTOR2_IN1_ = 0
_MOTOR2_IN2_ = 0

_SLEEP_TIME = 1


class Driver:
       
    def __init__(self):
        gpio = GPIO_Worker()
              
                
    def move_forward(self):
        #configure both GPIO pins or motor 1 for FWD movement
        self.gpio.set_gpio(_MOTOR1_IN1_,HIGH)
        self.gpio.set_gpio(_MOTOR1_IN2_,LOW)
        #configure both GPIO pins or motor 2 for FWD movement
        self.gpio.set_gpio(_MOTOR2_IN1_,HIGH)
        self.gpio.set_gpio(_MOTOR2_IN2_,LOW)
        
    def move_backword(self):
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR1_IN1_,LOW)
        self.gpio.set_gpio(_MOTOR1_IN2_,HIGH)
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR2_IN1_,LOW)
        self.gpio.set_gpio(_MOTOR2_IN2_,HIGH)    

    def move_left(self):
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR1_IN1_,HIGH)
        self.gpio.set_gpio(_MOTOR1_IN2_,LOW)
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR2_IN1_,LOW)
        self.gpio.set_gpio(_MOTOR2_IN2_,HIGH) 
        time.sleep(_SLEEP_TIME)
        #Stop vehicle
        self.gpio.set_gpio(_MOTOR1_IN1_,LOW)
        self.gpio.set_gpio(_MOTOR2_IN2_,LOW)        
   
    def move_right(self):
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR1_IN1_,LOW)
        self.gpio.set_gpio(_MOTOR1_IN2_,HIGH)
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR2_IN1_,HIGH)
        self.gpio.set_gpio(_MOTOR2_IN2_,LOW) 
        time.sleep(_SLEEP_TIME)
        self.gpio.set_gpio(_MOTOR1_IN2_,LOW)
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR2_IN1_,LOW)
        
    def stop(self):
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR1_IN1_,LOW)
        self.gpio.set_gpio(_MOTOR1_IN2_,LOW)
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR2_IN1_,LOW)
        self.gpio.set_gpio(_MOTOR2_IN2_,LOW) 

        
