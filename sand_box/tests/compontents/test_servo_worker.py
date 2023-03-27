##################################################
# AUTHOR                                         #
# SABARISH VIJAYAKUMAR                           #
##################################################
import sys
import time
import threading

sys.path.append('../../../')
from components.servo_worker import Servo_Worker

def control_rotation_by_20(channel):
    servo=Servo_Worker(channel)
    for i in range (180,0,-20):
        servo.set_angle(i)
        time.sleep(1)

def control_rotation_by_10(channel):
    servo=Servo_Worker(channel)
    for i in range (180,0,-10):
        servo.set_angle(i)
        time.sleep(1)

if __name__ == "__main__":
    servo_channel1 = threading.Thread(target=control_rotation_by_20,args={0,})
    servo_channel2 = threading.Thread(target=control_rotation_by_10,args={1,})
    servo_channel1.start()
    servo_channel2.start()
    