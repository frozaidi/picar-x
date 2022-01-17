import numpy as np
from sensor import GrayscaleSensor
from utils import reset_mcu
reset_mcu()


class Interpreter(object):
    def __init__(self, sensitivity=0, polarity=1):
        self.sensitivity = sensitivity
        self.polarity = polarity

    def edge_detect(self, gry_list):
        gry_list_norm = [float(i)/max(gry_list) for i in gry_list]
        gry_list_diff = max(gry_list_norm)-min(gry_list_norm)
        if gry_list_diff > self.sensitivity:
            rel_dir = gry_list_norm[0]-gry_list_norm[2]
            print("Relative Direction: "+str(rel_dir))
            error = (max(gry_list_norm)-np.mean(gry_list_norm))/0.7
            print("Error: "+str(error))
            rel_dir_pol = rel_dir*error*self.polarity

        return rel_dir_pol


if __name__ == '__main__':
    import time
    sens = GrayscaleSensor()
    inter = Interpreter(0.0, -1)

    while True:
        list = sens.get_grayscale_data()
        rel_dir = inter.edge_detect(list)
        print("{:.3f}".format(rel_dir))
        time.sleep(1)
