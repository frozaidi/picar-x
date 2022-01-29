# ROB 599 (Intro II): Picar-X

This repository is a fork of the Sunfounder's PicarX repository used for the ROB 599 (Intro II) course.

## Week 2 Code

The three files modified for Week 2 are as follows:

- `/scripts/movement_control.py`
- `/lib/picarx_improved.py`
- `/lib/sim_ezblock.py`

The `movement_control.py` is the main file used to control the PicarX robot. This script imports the `PicarX()` class from the `picarx_improved.py` file.

The `picarx_improved.py` file contains the necessary motor setup for controlling the movement of the PicarX robot.

The `sim_ezblock.py` file mimics the onboard utility functions that the PicarX robot uses when running scripts. This allows the user to run the movement scripts on a desktop environment without the need to connect to the PicarX robot.

## Week 3 Code

Three helper files were created for Week 3:

- `/lib/sensor.py`
- `/lib/interpreter.py`
- `/lib/controller.py`

The line following script, found in `/scripts/line_follow.py`, uses the above three helper functions to follow a line on the ground. Note that the grayscale sensors are actually IR transmitter/receivers. Therefore, some seemingly distinct combination of tape/ground might not actually work. This requires testing on different combinations.

The camera line following script, found in `/scripts/camera_lane_following.py`, uses code obtained from the [DeepPiCar article](https://towardsdatascience.com/deeppicar-part-4-lane-following-via-opencv-737dd9e47c96), alongside the PicarX computer vision code to follow a piece of blue tape. Note that due to the large amount of processing required, speeds of the PicarX should be kept to a minimum to allow for processing and turning of the wheels.

## Week 4 Code

Three helper methods were created for Week 3, within the following files:

- `/lib/sensor.py` under the `sensor_bus()` method
- `/lib/interpreter.py` under the `interpret_bus()` method
- `/lib/controller.py` under the `cont_bus()` method

The bus class was also implemented in `/lib/bus.py` which establishes the structure for a broadcast bus.

The line following script with concurrency is found in `/scripts/concurrent_line_follow.py`. This script uses the bus methods to perform concurrent line following.
