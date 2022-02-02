import concurrent.futures
import sys
sys.path.append(r'/home/frozaidi/picar-x/lib')
sys.path.append(r'/home/frozaidi/picar-x/rossros')
import rossros as rr                                    # noqa: E402
from picarx_improved import Picarx                      # noqa: E402
from interpreter import Interpreter                     # noqa: E402
from sensor import GrayscaleSensor                      # noqa: E402
from controller import Controller                       # noqa: E402
from interpreter_ult import UltrasonicInterpreter       # noqa: E402
from sensor_ult import UltrasonicSensor                 # noqa: E402
from controller_ult import UltrasonicController         # noqa: E402

if __name__ == '__main__':
    px = Picarx()
    scale = int(input("Enter scale [1,10]: "))
    polarity = int(input("Enter polarity (-1 or 1):"))
    speed = int(input("Enter max speed [0,100]:"))
    dist = int(input("Enter wall distance (cm):"))
    slow_rate = int(input("Enter rate of slow down [1,10]:"))

    con = Controller(px, scale)
    sens = GrayscaleSensor()
    inter = Interpreter(0.0, polarity)
    sens_bus = rr.Bus([1, 1, 1], "Grayscale Sensor Bus")
    inter_bus = rr.Bus(0, "Grayscale Interpreter Bus")
    term_bus = rr.Bus(0, "Termination Bus")

    sens_delay = 0.01
    inter_delay = 0.01
    cont_delay = 0.01
    term_delay = 0.01

    gry_sens = rr.Producer(sens.get_grayscale_data, sens_bus, sens_delay,
                           term_bus, "Grayscale Producer")

    gry_inter = rr.ConsumerProducer(inter.edge_detect, sens_bus, inter_bus,
                                    inter_delay, term_bus,
                                    "Grayscale Interpreter")

    gry_cont = rr.Consumer(con.line_follow, inter_bus, cont_delay, term_bus,
                           "Grayscale Controller")

    ult_cont = UltrasonicController(px, speed)
    ult_sens = UltrasonicSensor()
    ult_inter = UltrasonicInterpreter(dist, slow_rate)
    ult_sens_bus = rr.Bus(0, "Ultrasonic Sensor Bus")
    ult_inter_bus = rr.Bus(0, "Ultrasonic Interpreter Bus")

    ult_sensCP = rr.Producer(ult_sens.read, ult_sens_bus, sens_delay,
                             term_bus, "Ultrasonic Producer")

    ult_interCP = rr.ConsumerProducer(ult_inter.wall_detect, ult_sens_bus,
                                      ult_inter_bus, inter_delay, term_bus,
                                      "Ultrasonic Interpreter")

    ult_contCP = rr.Consumer(ult_cont.wall_avoid, ult_inter_bus, cont_delay,
                             term_bus, "Ultrasonic Controller")

    term_timer = rr.Timer(term_bus, 5, term_delay, term_bus,
                          "Termination Timer")

    with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
        eGrySensor = executor.submit(gry_sens)
        eGryInterp = executor.submit(gry_inter)
        eGryCont = executor.submit(gry_cont)
        eUltSensor = executor.submit(ult_sensCP)
        eUltInterp = executor.submit(ult_interCP)
        eUltCont = executor.submit(ult_contCP)
        eTimer = executor.submit(term_timer)

    eGrySensor.result()
    eGryInterp.result()
    eGryCont.result()
    eUltSensor.result()
    eUltInterp.result()
    eUltCont.result()
    eTimer.result()
