##################################################
# AUTHOR                                         #
# SABARISH VIJAYAKUMAR                           #
##################################################
import sys
import time
import threading

sys.path.append('../../components')
from rotation_manager import Rotation_Manager

def controlRotationBy20(channel):
    rotation=Rotation_Manager(channel)
    for i in range (180,0,-20):
        rotation.setAngle(i)
        time.sleep(1)

def controlRotationBy10(channel):
    rotation=Rotation_Manager(channel)
    for i in range (180,0,-10):
        rotation.setAngle(i)
        time.sleep(1)

if __name__ == "__main__":
    servo_channel1 = threading.Thread(target=controlRotationBy20,args={0,})
    servo_channel2 = threading.Thread(target=controlRotationBy10,args={1,})
    servo_channel1.start()
    servo_channel2.start()
    