'''
    this code keeps led on untill the button is pressed again modifying it is almost same as modifying arduino code but keep in mind of gpio pins
'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led=4;btn=27
GPIO.setup(led,GPIO.OUT)
GPIO.setup(btn,GPIO.IN)
count=0
while True:    
    if GPIO.input(btn)==GPIO.HIGH:
       count+=1
    
    if count%2==0:
        GPIO.output(led,GPIO.HIGH)
    else:
        GPIO.output(led,GPIO.LOW)
    time.sleep(.05)
    
GPIO.cleanup()