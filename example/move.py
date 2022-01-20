import time
import sys
sys.path.append(r'/home/frozaidi/picar-x/lib')
try:
    from picarx_improved import Picarx
    from utils import reset_mcu
    reset_mcu()
    time.sleep(0.01)
except (ImportError, ModuleNotFoundError, NameError):
    print("This computer does not appear to be a PiCar-X system (ezblock is "
          "not present). Shadowing hardware calls with substitute functions")
    from sim_ezblock import *


if __name__ == "__main__":
    try:
        px = Picarx()
        px.forward(30)
        time.sleep(0.5)
        for angle in range(0, 35):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        for angle in range(35, -35, -1):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        for angle in range(-35, 0):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        px.forward(0)
        time.sleep(1)

        for angle in range(0, 35):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(35, -35, -1):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(-35, 0):
            px.set_camera_servo1_angle(angle)
            time.sleep(0.01)
        for angle in range(0, 35):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)
        for angle in range(35, -35, -1):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)
        for angle in range(-35, 0):
            px.set_camera_servo2_angle(angle)
            time.sleep(0.01)

    finally:
        px.forward(0)
