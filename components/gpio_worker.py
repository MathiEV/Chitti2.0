##################################################
# AUTHOR                                         #
# SABARISH VIJAYAKUMAR                           #
##################################################
import RPi.GPIO as GPIO
from application_modules.logger_module import Logger_Module

class GPIO_Worker:
    _logger = Logger_Module();
    _def_pin_config = {
        5:GPIO.OUT,
        6:GPIO.OUT,    
        16:GPIO.OUT,
        19:GPIO.OUT,
        20:GPIO.OUT,
        21:GPIO.IN,
        23:GPIO.OUT,
        24:GPIO.OUT,
        26:GPIO.OUT,
        25:GPIO.OUT        
        }
        
    def __init__(self):
        self._logger.logDebug("GPIO worker init started")
        GPIO.setmode(GPIO.BCM)        
        for pin, mode in  self._def_pin_config.items():            
            GPIO.setup(pin, mode)        
        self._logger.logDebug("GPIO worker init completed")
        
    def set_gpio(self, pin, state):
        GPIO.output(pin,state)
    
    def get_gpio(self, pin):
        return GPIO.input(pin)
