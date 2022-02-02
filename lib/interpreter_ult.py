import numpy as np


class UltrasonicInterpreter(object):
    def __init__(self, limit=10, slow_rate=5):
        """
        Initialize the ultrasonic interpreter class
        :param limit: the desired stopping limit in cm
        :param slow_rate: the rate of slowing down the car, higher numbers
        indicate a slower "slowdown" rate
        """
        self.limit = limit
        self.slow_rate = slow_rate

    def wall_detect(self, distance):
        """
        Based on the desired stopping limit, the function outputs a relative
        direction from [-1,1], where -1 dictates a backwards movement
        :param distance: the current distance of the PicarX from the wall
        """
        rel_dir = np.tanh((distance-self.limit)/self.slow_rate)

        return rel_dir
