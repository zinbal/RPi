'''
    this code blinks led by keeping it on for 1.5 sec and offfor 1 sec you can change these value from below time.sleep function
    Just connect led with GPIO pin 4 and a resistor of 220 ohm or better go with color code for resistors
'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led=4
GPIO.setup(led,GPIO.OUT)
try:
    for i in range(0,5):    
        GPIO.output(led,GPIO.HIGH)
        time.sleep(1.5)
        GPIO.output(led,GPIO.LOW)
        time.sleep(1)
    GPIO.cleanup()
except:
    GPIO.cleanup()
