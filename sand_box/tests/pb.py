import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.IN)
while(1):
	if(GPIO.input(13)==True):
		GPIO.output(11,True)
		print 'on'
	else:
		GPIO.output(11,False)
		print 'off'
 
