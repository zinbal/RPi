'''
    this code snippet here allows you to gather the photographs whenever there is a security breach
    for thiss youjust need to connect your camera module
'''

from picamera import PiCamera
import time

camera=PiCamera()
camera.resolution= (1280,1080)
camera.rotation=180
time.sleep(2)

fn="/home/pi/Desktop/2/"
for i in range(0,10):
    a=fn+str(i)+".jpg"
    camera.capture(a)
    print("complete")
