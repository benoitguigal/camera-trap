# -*- coding: utf8 -*-
import logging
import time


logger = logging.getLogger(__name__)


class App(object):

    def __init__(self):
        pass

    def start(self):
        logger.info("Starting app")
        while True:
            logger.info("Waiting for a deer")
            time.sleep(5)

    def stop(self):
        logger.info("Bye Bye")



