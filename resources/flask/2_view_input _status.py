'''
    Connect button at GPIO pin number 17
    change port to the port thats not in use
    run this code
    
    enter url as 127.0.0.1 or your ip address
    go to 127.0.0.1/17 to see button status
    
'''

from flask import Flask
import RPi.GPIO as GPIO

btn=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn,GPIO.IN)

app = Flask(__name__)

@app.route("/")

def index():
    a='hop to /17 to see btn status at GPIO 17 ' 
    return a

@app.route("/17")
def get_input():
    a=GPIO.input(btn)
    if a==GPIO.HIGH:
        b= "button at 17 is PRESSED"
    else:
        b= "button at 17 is NOT PRESSED"
        
    return b

try:
    app.run(port=8000)
    GPIO.cleanup()
except:
    GPIO.cleanup()

