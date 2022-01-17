'''
    this code snippet here allows you to gather the photographs whenever there is a security breach
    for thiss youjust need to connect your camera module
'''

from picamera import PiCamera
import time


camera=PiCamera()
camera.resolution = (1920,1080)
camera.rotation=180
time.sleep(2)

fn="/home/pi/Desktop/threat.jpg"
camera.capture(fn)
print("complete")
