import time
from picarx_improved import Picarx
from interpreter import Interpreter
from sensor import GrayscaleSensor
from controller import Controller
from utils import reset_mcu
reset_mcu()

if __name__ == '__main__':
    px = Picarx()
    scale = input("Enter scale: ")
    polarity = input("Enter polarity:")
    con = Controller(scale)
    sens = GrayscaleSensor()
    inter = Interpreter(0.0, polarity)

    while True:
        list = sens.get_grayscale_data()
        rel_dir = inter.edge_detect(list)
        angle = con.line_follow(px, rel_dir)
        print("Steering angle: "+str(angle))
        time.sleep(0.5)
