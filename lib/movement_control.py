import time
from picarx_improved import Picarx


def drive(picarx, dir="forward", angle=0, sleep=5, speed=100):
    picarx.set_dir_servo_angle(angle)
    if dir == "forward":
        picarx.forward(speed)
        time.sleep(sleep)
    elif dir == "backward":
        picarx.backward(speed)
        time.sleep(sleep)
    else:
        print("Not a valid direction. Try again.")


def parallel_parking(picarx, dir="left", sleep=1):
    if dir == "left":
        picarx.set_dir_servo_angle(-40)
        picarx.backward(100)
        time.sleep(sleep)
        picarx.set_dir_servo_angle(40)
        time.sleep(sleep)
        picarx.forward(100)
        time.sleep(sleep/2)
        picarx.stop()
    elif dir == "right":
        picarx.set_dir_servo_angle(40)
        picarx.backward(100)
        time.sleep(sleep)
        picarx.set_dir_servo_angle(-40)
        time.sleep(sleep)
        picarx.forward(100)
        time.sleep(sleep/2)
        picarx.stop()
    else:
        print("Not a valid direction. Try again.")


def k_turn(picarx, dir="left", sleep=1):
    if dir == "left":
        picarx.set_dir_servo_angle(-40)
        picarx.forward(100)
        time.sleep(sleep)
        picarx.set_dir_servo_angle(40)
        picarx.backward(100)
        time.sleep(sleep)
        picarx.set_dir_servo_angle(-40)
        picarx.forward(100)
        time.sleep(sleep)
        picarx.stop()
    elif dir == "right":
        picarx.set_dir_servo_angle(40)
        picarx.forward(100)
        time.sleep(sleep)
        picarx.set_dir_servo_angle(-40)
        picarx.backward(100)
        time.sleep(sleep)
        picarx.set_dir_servo_angle(40)
        picarx.forward(100)
        time.sleep(sleep)
        picarx.stop()
    else:
        print("Not a valid direction. Try again.")


if __name__ == '__main__':
    px = Picarx()
    flag = False
    while flag is False:
        maneuver = input("Select maneuver type [drive/parallel/kturn]: ")
        if maneuver == "drive":
            dir = input("Input direction [forward/backward]: ")
            angle = int(input("Input angle [-40,40]: "))
            sleep = int(input("Input duration of drive (seconds): "))
            speed = abs(int(input("Set the speed [0,100]: ")))
            drive(px, dir, angle, sleep, speed)
        elif maneuver == "parallel":
            dir = input("Input direction [left/right]: ")
            sleep = int(input("Input duration of movement (seconds): "))
            parallel_parking(px, dir, sleep)
        elif maneuver == "kturn":
            dir = input("Input direction [left/right]: ")
            sleep = int(input("Input duration of movement (seconds): "))
            k_turn(px, dir, sleep)
        else:
            print("Invalid maneuver, try again, you absolute fool.")
        continue_maneuver = input("Try another maneuver [y/n]? ")
        if continue_maneuver == "y":
            continue
        elif continue_maneuver == "n":
            flag = True
        else:
            print("Invalid response. Terminating program, you fool.")
            flag = True
