# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 19:00:05 2023

AUTHOR                                         
Krushna kumar V                                
"""
import time

from components.gpio_worker import GPIO_Worker

#Motor1 right
_MOTOR1_IN1_ = 5 
_MOTOR1_IN2_ = 6
_MOTOR2_IN1_ = 19
_MOTOR2_IN2_ = 13

_SLEEP_TIME = 1


class Vehicle:
       
    def __init__(self):
        self.gpio = GPIO_Worker()
              
                
    def move_forward(self):
        print("Moving forward")
        #configure both GPIO pins or motor 1 for FWD movement
        self.gpio.set_gpio(_MOTOR1_IN1_,True)
        self.gpio.set_gpio(_MOTOR1_IN2_,False)
        #configure both GPIO pins or motor 2 for FWD movement
        self.gpio.set_gpio(_MOTOR2_IN1_,True)
        self.gpio.set_gpio(_MOTOR2_IN2_,False)
        
        
    def move_backward(self):
        print("Moving backward")
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR1_IN1_,False)
        self.gpio.set_gpio(_MOTOR1_IN2_,True)
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR2_IN1_,False)
        self.gpio.set_gpio(_MOTOR2_IN2_,True)    

    def move_left(self):
        print("Moving left")
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR1_IN1_,True)
        self.gpio.set_gpio(_MOTOR1_IN2_,False)
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR2_IN1_,False)
        self.gpio.set_gpio(_MOTOR2_IN2_,True) 
        time.sleep(_SLEEP_TIME)
        #Stop vehicle
        self.gpio.set_gpio(_MOTOR1_IN1_,False)
        self.gpio.set_gpio(_MOTOR2_IN2_,False)        
   
    def move_right(self):
        print("Moving right")
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR1_IN1_,False)
        self.gpio.set_gpio(_MOTOR1_IN2_,True)
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR2_IN1_,True)
        self.gpio.set_gpio(_MOTOR2_IN2_,False) 
        time.sleep(_SLEEP_TIME)
        self.gpio.set_gpio(_MOTOR1_IN2_,False)
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR2_IN1_,False)
        
    def stop(self):
        print("stop")
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR1_IN1_,False)
        self.gpio.set_gpio(_MOTOR1_IN2_,False)
        #configure both GPIO pins for motor1
        self.gpio.set_gpio(_MOTOR2_IN1_,False)
        self.gpio.set_gpio(_MOTOR2_IN2_,False) 

        
