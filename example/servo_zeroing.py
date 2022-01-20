import time
import sys
sys.path.append(r'/home/frozaidi/picar-x/lib')
try:
    from servo import Servo
    from pwm import PWM
    from utils import reset_mcu
    reset_mcu()
    time.sleep(0.01)
except (ImportError, ModuleNotFoundError, NameError):
    print("This computer does not appear to be a PiCar-X system (ezblock is "
          "not present). Shadowing hardware calls with substitute functions")
    from sim_ezblock import *


if __name__ == '__main__':
    P_11 = Servo(PWM('P11'))
    P_11.angle(0)
