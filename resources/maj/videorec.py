'''
    this code snippet here allows you to record video whenever there is a security breach
    for thiss you just need to connect your camera module
'''

from picamera import PiCamera
import time


camera=PiCamera()
camera.resolution = (1280,1080)
camera.rotation=180
time.sleep(2)

fn="/home/pi/Desktop/video.h264"
camera.start_recording(fn)
camera.wait_recording(5)
camera.stop_recording()
print("complete")
