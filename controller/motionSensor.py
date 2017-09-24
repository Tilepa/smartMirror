import sys
import time
from model.configurations import SENSOR_PIN

try:
    import RPi.GPIO as GPIO
except ImportError:
    flags = None


motion = 0


def start_motion_detection():
    if sys.platform.startswith("linux"):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SENSOR_PIN, GPIO.IN)

        GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=motion_detected)
        while True:
            time.sleep(30)

            check_for_motion()
        GPIO.cleanup()


def motion_detected(channel):
    if sys.platform.startswith('linux'):
        print('Es gab eine Bewegung!')
        global motion
        motion = 1

        check_for_motion()


def check_for_motion():
    global motion

    if motion == 1:
        show_ui()
        motion = 0
    else:
        shut_down_ui()


def show_ui():
    if sys.platform.startswith('linux'):
        import os
        os.system("xset dpms force on")
    print("show")


def shut_down_ui():
    if sys.platform.startswith('linux'):
        import os
        os.system("xset dpms force off")
    print("close")