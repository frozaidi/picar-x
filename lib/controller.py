import time
from picarx_improved import Picarx
from interpreter import Interpreter
from sensor import GrayscaleSensor
from utils import reset_mcu
reset_mcu()


class Controller(object):
    def __init__(self, scale=40):
        self.scale = scale

    def line_follow(self, px, rel_dir):
        self.steer_angle = -1*rel_dir*self.scale
        px.set_dir_servo_angle(self.steer_angle)

        return self.steer_angle


if __name__ == '__main__':
    px = Picarx()
    con = Controller()
    sens = GrayscaleSensor()
    inter = Interpreter(0.0, -1)

    while True:
        list = sens.get_grayscale_data()
        rel_dir = inter.edge_detect(list)
        angle = con.line_follow(px, rel_dir)
        print("Steering angle: "+str(angle))
        time.sleep(0.5)
