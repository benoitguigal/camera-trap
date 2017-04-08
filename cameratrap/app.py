# -*- coding: utf8 -*-
import logging
import time
import signal

from .devices.sensors import InfraredSensor
from .devices.camera import Camera

logger = logging.getLogger(__name__)


class App(object):

    def __init__(self):
        self.infrared_sensor = None
        self.camera = None

    def initialize_devices(self):
        self.infrared_sensor = InfraredSensor()
        self.infrared_sensor.when_activated = self.when_infrared_sensor_is_activated
        self.camera = Camera()

    def when_infrared_sensor_is_activated(self, _):
        logger.info("Infrared sensor activated")
        self.camera.capture()
        time.sleep(3)

    def start(self):
        logger.info("Starting app")
        self.initialize_devices()
        signal.pause()

    def stop(self):
        logger.info("Bye Bye")



