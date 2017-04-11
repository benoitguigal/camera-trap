# -*- coding: utf8 -*-
import logging
from datetime import datetime
import time

import RPi.GPIO as GPIO
import picamera


camera = picamera.PiCamera()

date_fmt = "%Y%m%dT%H:%M:%S"


def callback_up(channel):
    print("We detected something !")
    now = datetime.now()
    now_str = now.strftime(date_fmt)
    filepath = "/mnt/storage/%s.jpg" % str(now_str)
    camera.capture(filepath)
    time.sleep(5)


class App(object):

    def start(self):
        print("Starting app")
        pin_number = 4
        GPIO.setmode(GPIO. BCM)
        GPIO.setup(pin_number, GPIO.IN)
        GPIO.add_event_detect(pin_number, GPIO.RISING, callback=callback_up)

    def stop(self):
        print("Bye Bye")