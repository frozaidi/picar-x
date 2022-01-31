import concurrent.futures
import sys
sys.path.append(r'/home/frozaidi/picar-x/lib')
sys.path.append(r'/home/frozaidi/picar-x/rossros')
import rossros as rr                    # noqa: E402
from picarx_improved import Picarx      # noqa: E402
from interpreter import Interpreter     # noqa: E402
from sensor import GrayscaleSensor      # noqa: E402
from controller import Controller       # noqa: E402

if __name__ == '__main__':
    px = Picarx()
    scale = int(input("Enter scale: "))
    polarity = int(input("Enter polarity:"))
    con = Controller(px, scale)
    sens = GrayscaleSensor()
    inter = Interpreter(0.0, polarity)
    sens_bus = rr.Bus([1,1,1], "Grayscale Sensor Bus")
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

    term_timer = rr.Timer(term_bus, 5, term_delay, term_bus,
                          "Termination Timer")

    px.forward(40)

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        eGrySensor = executor.submit(gry_sens)
        eGryInterp = executor.submit(gry_inter)
        eGryCont = executor.submit(gry_cont)
        eTimer = executor.submit(term_timer)

    eGrySensor.result()
    eGryInterp.result()
    eGryCont.result()
    eTimer.result()
