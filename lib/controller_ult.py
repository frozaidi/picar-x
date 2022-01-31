

class UltrasonicController(object):
    def __init__(self, px, max_speed=50):
        self.max_speed = max_speed
        self.px = px

    def wall_avoid(self, rel_dir):
        self.speed = self.px.forward(self.max_speed*rel_dir)
        return self.speed
