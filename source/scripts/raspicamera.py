from picamera import PiCamera
from time import sleep
import time
camera = PiCamera()

# Camera Settings
# Available resolutions '800x600','1024x786','1900x1200','1280x720','1920x1080'$
camera.resolution = (2592, 1944)
camera.framerate = 30  # 2-30fps
camera.exposure_mode = 'auto'  # Available exposure modes 'auto', 'night', 'nig$
camera.awb_mode = 'auto'  # Available white balance modes 'off', 'auto', 'sun',$
camera.ISO = 800  # ISO (100 - 800)

# Capture the image and save it
file_name = "/home/pi/payload_files/img_" + str(time.time()) + ".jpg"
camera.capture(file_name)

print("file saved to:",file_name)