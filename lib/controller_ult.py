

class UltrasonicController(object):
    def __init__(self, px, max_speed=50):
        """
        Initialize the ultrasonic controller to control the speed of the Picar
        :param px: the PicarX object
        :param max_speed: the max speed of the Picar [0,100]
        """
        self.max_speed = max_speed
        self.px = px

    def wall_avoid(self, rel_dir):
        """
        Function to use the relative direction given by the interpreter to
        change the speed of the Picar
        :param rel_dir: the relative direction given by the interpreter
        """
        self.speed = self.px.forward(self.max_speed*rel_dir)
        return self.speed
