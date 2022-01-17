from servo import Servo
from pwm import PWM
from utils import reset_mcu
import sys
sys.path.append(r'/home/frozaidi/picar-x/lib')
reset_mcu()


if __name__ == '__main__':
    P_11 = Servo(PWM('P11'))
    P_11.angle(0)
