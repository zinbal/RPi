import RPi.GPIO as GPIO
import time
 
led = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)
pwm = GPIO.PWM(led, 1000)
pwm.start(0)
try:
    for dc in range(0, 101):
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.05)
    time.sleep(1)
    GPIO.cleanup()

except:
    GPIO.cleanup()
