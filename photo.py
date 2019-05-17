from gpiozero import Button
from picamera import PiCamera
from time import sleep
from subprocess import call
 
camera = PiCamera()
button = Button(4)
def take_picture_with_camera():
    camera.start_preview(alpha=190)
    sleep(1)
    camera.capture('/home/pi/photo/image.jpg')
    camera.stop_preview()
    
button.when_pressed = take_picture_with_camera
sleep(10)
 
call(["python", "text_recognition.py"])