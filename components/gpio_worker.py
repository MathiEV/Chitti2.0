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
        13:GPIO.OUT,
        19:GPIO.OUT,
        12:GPIO.IN,
        20:GPIO.IN,
        23:GPIO.IN,
        16:GPIO.OUT,    
        21:GPIO.OUT,
        24:GPIO.OUT        
        }
        
    def __init__(self):    
        self._logger.logDebug("GPIO worker init started")
        GPIO.setmode(GPIO.BCM)        
        for pin, mode in  self._def_pin_config.items():            
            GPIO.setup(pin, mode)
            if GPIO.OUT == mode :
                GPIO.output(pin, False)
        self._logger.logDebug("GPIO worker init completed")
        
    def set_gpio(self, pin, state):
        GPIO.output(pin,state)
    
    def get_gpio(self, pin):
        return GPIO.input(pin)
    
    def clean_up(self):
        for pin, mode in  self._def_pin_config.items():            
            if GPIO.OUT == mode :
                GPIO.output(pin, False)
        GPIO.cleanup()
