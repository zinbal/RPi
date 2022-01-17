import RPi.GPIO as GPIO
import time
maxd=200; mind=4
TRIG=21;ECHO=20
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
try:
    while True:
        print("measuring distance")
        
        GPIO.output(TRIG,False)
        time.sleep(0.2)
        GPIO.output(TRIG,True)
        time.sleep(0.00001) #10us for wait
        GPIO.output(TRIG,False)
        
        while GPIO.input(ECHO)==0:
            pulse_start=time.time()
        while GPIO.input(ECHO)==1:
            pulse_end=time.time()
        pulse_duration=pulse_end-pulse_start        #calculate time taken
        
        distance=pulse_duration*17150               #calculate distance
        distance=round(distance,2)                  #round off to 2nd decimal value
        
        if (distance<mind):
            distance="too close"
        elif (distance>maxd):
            distance="too far"
            
        print("distance:",distance,"cm")
        
        time.sleep(1)
except:
    GPIO.cleanup()
