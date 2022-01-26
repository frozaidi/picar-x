import time
import concurrent.futures
import sys
sys.path.append(r'/home/frozaidi/picar-x/lib')
try:
    from picarx_improved import Picarx
    from interpreter import Interpreter
    from sensor import GrayscaleSensor
    from controller import Controller
    from bus import Bus
except ModuleNotFoundError:
    pass

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
    sens_bus = Bus()
    inter_bus = Bus()
    sens_delay = 0.01
    inter_delay = 0.01
    cont_delay = 0.01

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        eSensor = executor.submit(sens.sensor_bus,
                                  sens_bus, sens_delay)
        eInterpreter = executor.submit(inter.inter_bus,
                                       sens_bus, inter_bus, inter_delay)
        eController = executor.submit(con.cont_bus,
                                      px, inter_bus, cont_delay)
    eSensor.result()
    eInterpreter.result()
    eController.result()
