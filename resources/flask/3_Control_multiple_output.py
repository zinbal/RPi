'''
    Connect 3 leds at GPIO pin number 17, 27,22
    change port to the port thats not in use
    run this code
    
    enter url as 127.0.0.1 or your ip address
'''


from flask import Flask
import RPi.GPIO as GPIO

led=[17,27,22]

GPIO.setmode(GPIO.BCM)


for i in led:
    GPIO.setup(i,GPIO.OUT)
for i in led:
    GPIO.output(i,GPIO.LOW)


app = Flask(__name__)

@app.route("/")

def index():
    a='use /led/ledpin/state/ledstate \n where led pin needs to be one of [17,27,22,255] \n where 255 means all pin followed by state and state needs to be one of [0,1] ' 
    return a


@app.route("/led/<int:ledp>/state/<int:state>")
def ledt(ledp,state):
    if ledp in led:
        if state==0:
            GPIO.output(ledp,GPIO.LOW)
            k= "low"
        elif state==1:
            GPIO.output(ledp,GPIO.HIGH)
            k= "high"
        else:
            k= "Return 0 or 1 "
    

    elif ledp==255:
        if state==0:
            for i in led:
                GPIO.output(i,GPIO.LOW)
            k= "all leds are LOW"
        elif state==1:
            for i in led:
                GPIO.output(i,GPIO.HIGH)
            k= "all leds are HIGH"
        else:
            k= "Return 0 or 1 "
        
    else:
        k= "choose valid led pin"
    return k

app.run(port=8000)

GPIO.cleanup()
