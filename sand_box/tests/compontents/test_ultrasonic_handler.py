##################################################
# AUTHOR                                         #
# SABARISH VIJAYAKUMAR                           #
##################################################
import sys
import time

sys.path.append('../../../')
from components.ultrasonic_handler import Ultrasonic_Handler

ultrasonic_handler = Ultrasonic_Handler()

while True:
    ultrasonic_handler.check_for_obstacles()
    time.sleep(1)