# -*- coding: utf8 -*-
import logging
from datetime import datetime
import time

import RPi.GPIO as GPIO
import picamera


logger = logging.getLogger(__name__)

camera = picamera.PiCamera()


def callback_up(channel):
    logger.info("We detected something !")
    now = datetime.now()
    filepath = "/mnt/storage/%s.jpg" % str(now)
    camera.capture(filepath)
    time.sleep(5)


class App(object):

    def start(self):
        logger.info("Starting app")
        pin_number = 4
        GPIO.setmode(GPIO. BCM)
        GPIO.setup(pin_number, GPIO.IN)
        GPIO.add_event_detect(pin_number, GPIO.RISING, callback=callback_up)

    def stop(self):
        logger.info("Bye Bye")



