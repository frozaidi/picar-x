import time
from picarx_improved import Picarx
from interpreter import Interpreter
from sensor import GrayscaleSensor
from controller import Controller

if __name__ == '__main__':
    """
    This script imports all helper functions and follows a line while moving
    forwards at a constant speed
    """
    px = Picarx()
    scale = int(input("Enter scale: "))
    polarity = int(input("Enter polarity:"))
    con = Controller(scale)
    sens = GrayscaleSensor()
    inter = Interpreter(0.0, polarity)

    while True:
        list = sens.get_grayscale_data()
        rel_dir = inter.edge_detect(list)
        angle = con.line_follow(px, rel_dir)
        print("Steering angle: "+str(angle))
        px.forward(40)
        time.sleep(0.1)
