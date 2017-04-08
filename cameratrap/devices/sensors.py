# -*- coding: utf8 -*-
import inspect
from functools import wraps
import RPi.GPIO as GPIO


class BadEventHandler(Exception):
    pass


class InfraredSensor(object):

    def __init__(self):
        self._when_activated = None
        pin_number = 4
        GPIO.setmode(GPIO. BCM)
        GPIO.setup(pin_number, GPIO.IN)
        GPIO.add_event_detect(pin_number, GPIO.RISING, callback=self.when_activated)

    @property
    def when_activated(self):
        return self._when_activated

    @when_activated.setter
    def when_activated(self, value):
        self._when_activated = self._wrap_callback(value)

    def _wrap_callback(self, fn):
        if fn is None:
            return None
        elif not callable(fn):
            raise BadEventHandler('value must be None or a callable')
        elif inspect.isbuiltin(fn):
            # We can't introspect the prototype of builtins. In this case we
            # assume that the builtin has no (mandatory) parameters;
            return fn
        else:
            # Try binding ourselves to the argspec of the provided callable.
            # If this works, assume the function is capable of accepting no
            # parameters
            try:
                inspect.getcallargs(fn)
                return fn
            except TypeError:
                try:
                    # If the above fails, try binding with a single parameter
                    # (ourselves). If this works, wrap the specified callback
                    inspect.getcallargs(fn, self)
                    @wraps(fn)
                    def wrapper():
                        return fn(self)
                    return wrapper
                except TypeError:
                    raise BadEventHandler(
                        'value must be a callable which accepts up to one '
                        'mandatory parameter')
