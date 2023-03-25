import time
import Rpi.GPIO as GPIO
#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
print "Led on"
GPIO.output(2,True)
sleep(2)
print "Led on"
GPIO.output(2,False)
GPIO.cleanup()
