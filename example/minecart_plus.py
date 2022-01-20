import time
import sys
sys.path.append(r'/home/frozaidi/picar-x/lib')
try:
    from picarx_improved import Picarx
    from grayscale_module import Grayscale_Module
    from utils import reset_mcu
    reset_mcu()
    time.sleep(0.01)
except (ImportError, ModuleNotFoundError, NameError):
    print("This computer does not appear to be a PiCar-X system (ezblock is "
          "not present). Shadowing hardware calls with substitute functions")
    from sim_ezblock import *


if __name__ == '__main__':
    try:
        gm = Grayscale_Module(500)
        px = Picarx()
        px_power = 10
        while True:
            gm_val_list = gm.get_grayscale_data()
            print("gm_val_list:", gm_val_list)
            gm_status = gm.get_line_status(gm_val_list)
            print("gm_status:", gm_status)

            if gm_status == 'forward':
                print(1)
                px.forward(px_power)

            elif gm_status == 'left':
                px.set_dir_servo_angle(12)
                px.forward(px_power)

            elif gm_status == 'right':
                px.set_dir_servo_angle(-12)
                px.forward(px_power)
            else:
                px.set_dir_servo_angle(0)
                px.stop()

    finally:
        px.stop()
