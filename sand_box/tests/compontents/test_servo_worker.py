##################################################
# AUTHOR                                         #
# SABARISH VIJAYAKUMAR                           #
##################################################
import sys
import time
import threading

sys.path.append('../../components')
from servo_worker import Servo_Worker

def controlRotationBy20(channel):
    servo=Servo_Worker(channel)
    for i in range (180,0,-20):
        servo.setAngle(i)
        time.sleep(1)

def controlRotationBy10(channel):
    servo=Servo_Worker(channel)
    for i in range (180,0,-10):
        servo.setAngle(i)
        time.sleep(1)

if __name__ == "__main__":
    servo_channel1 = threading.Thread(target=controlRotationBy20,args={0,})
    servo_channel2 = threading.Thread(target=controlRotationBy10,args={1,})
    servo_channel1.start()
    servo_channel2.start()
    