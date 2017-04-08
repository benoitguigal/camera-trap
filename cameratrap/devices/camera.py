
import picamera


class Camera(object):

    def __init__(self):
        self._camera = picamera.PiCamera()

    def capture(self):
        self._camera.capture("image.jpg")
        # TODO save it to USB