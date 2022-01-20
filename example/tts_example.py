import sys
sys.path.append(r'/home/frozaidi/picar-x/lib')
try:
    from tts import TTS
except (ImportError, ModuleNotFoundError, NameError):
    print("This computer does not appear to be a PiCar-X system (ezblock is "
          "not present). Shadowing hardware calls with substitute functions")
    from sim_ezblock import *


if __name__ == "__main__":
    words = ["Hello", "Hi", "Good bye", "Nice to meet you"]
    tts_robot = TTS()
    for i in words:
        print(i)
        tts_robot.say(i)
