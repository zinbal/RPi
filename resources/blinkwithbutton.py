'''
    this code keeps led on till the button is pressed  modifying it is almost same as modifying arduino code but keep in mind of gpio pins
    connect your push button with a +3.3v , a resistor of 3.3 K ohm going to grnd and oine point to GPIO pin 17
    connect led with 220ohm resistance to common grnd and other otput to GPIO pin 4
'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led=4;btn=17
GPIO.setup(led,GPIO.OUT)
GPIO.setup(btn,GPIO.IN)
try:
    while True:    
        if GPIO.input(btn)==GPIO.HIGH:
            GPIO.output(led,GPIO.HIGH)
        else:
            GPIO.output(led,GPIO.LOW)
        time.sleep(.05)
        
    GPIO.cleanup()
except:
    GPIO.cleanup()
