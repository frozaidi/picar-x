import time
from picarx_improved import Picarx
from interpreter import Interpreter
from sensor import GrayscaleSensor


class Controller(object):
    def __init__(self, scale=1):
        # Set a scale to the [-1,1] range of direction given by the interpreter
        # which matches the maximum angle of the PicarX robot
        self.scale = scale*40

    def line_follow(self, px, rel_dir):
        """
        Function to set the steering angle based on the direction and scale
        :param px: The Picarx object, used to command the steering angle
        :param rel_dir: The relative direction of the line, [-1,1], where
        positive values indicate the line left of the robot
        """
        self.steer_angle = -1*rel_dir*self.scale
        px.set_dir_servo_angle(self.steer_angle)
        # Return the steer angle as feedback
        return self.steer_angle


if __name__ == '__main__':
    px = Picarx()
    con = Controller(2)
    sens = GrayscaleSensor()
    inter = Interpreter(0.0, -1)

    while True:
        list = sens.get_grayscale_data()
        rel_dir = inter.edge_detect(list)
        angle = con.line_follow(px, rel_dir)
        print("Steering angle: "+str(angle))
        time.sleep(0.5)
