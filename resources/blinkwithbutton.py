'''
    this code keeps led on till the button is pressed  modifying it is almost same as modifying arduino code but keep in mind of gpio pins
    Connect your push button with a +3.3V, a resistor of 3.3K ohm going to grounf and one point to GPIO pin 17
    Connect lef with 220 ohm resistance to common grnd and other output to GPIO pin 4
'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led=4;btn=27
GPIO.setup(led,GPIO.OUT)
GPIO.setup(btn,GPIO.IN)
while True:    
    if GPIO.input(btn)==GPIO.HIGH:
        GPIO.output(led,GPIO.HIGH)
    else:
        GPIO.output(led,GPIO.LOW)
    time.sleep(.05)
    
GPIO.cleanup()
