import time
from pin import Pin


class UltrasonicSensor():
    def __init__(self, timeout=0.02):
        self.trig = Pin("D2")
        self.echo = Pin("D3")
        self.timeout = timeout

    def _read(self):
        """
        Function reads the ultrasonic sensor values and converts it to cm
        """
        self.trig.low()
        time.sleep(0.01)
        self.trig.high()
        time.sleep(0.00001)
        self.trig.low()
        pulse_end = 0
        pulse_start = 0
        timeout_start = time.time()
        while self.echo.value() == 0:
            pulse_start = time.time()
            if pulse_start - timeout_start > self.timeout:
                return -1
        while self.echo.value() == 1:
            pulse_end = time.time()
            if pulse_end - timeout_start > self.timeout:
                return -1
        during = pulse_end - pulse_start
        cm = round(during * 340 / 2 * 100, 2)
        return cm

    def read(self, times=10):
        """
        Function calls _read command a specified amount of times in case of
        poor sensor readings, or sensor errors
        :param times: the number of times that the function calls _read
        """
        for i in range(times):
            a = self._read()
            if a != -1 or a <= 300:
                return a
        return -1
