'''
    this code blinks led by keeping it on for 1.5 sec and offfor 1 sec you can change these value from below time.sleep function
'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led=4
GPIO.setup(led,GPIO.OUT)
for i in range(0,10):    
    GPIO.output(led,GPIO.HIGH)
    time.sleep(1.5)
    GPIO.output(led,GPIO.LOW)
    time.sleep(1)
GPIO.cleanup()
