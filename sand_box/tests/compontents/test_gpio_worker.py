##################################################
# AUTHOR                                         #
# SABARISH VIJAYAKUMAR                           #
##################################################
import sys
import time

sys.path.append('../../../')
from components.gpio_worker import GPIO_Worker

def controlGPIO():
    gpio=GPIO_Worker()
    while True:                
        gpio.set_gpio(16,True)
        time.sleep(1)
        print("Get GPIO after set HIGH '"+str(gpio.get_gpio(21)) + "'")
        time.sleep(1)
        gpio.set_gpio(16,False)
        time.sleep(1)
        print("Get GPIO after set LOW '"+str(gpio.get_gpio(21)) + "'")        
        time.sleep(1)        

if __name__ == "__main__":
    controlGPIO()