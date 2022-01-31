import numpy as np


class UltrasonicInterpreter(object):
    def __init__(self, limit=10, slow_rate=5):
        self.limit = limit
        self.slow_rate = slow_rate

    def wall_detect(self, distance):
        rel_dir = np.tanh((distance-self.limit)/self.slow_rate)

        return rel_dir
