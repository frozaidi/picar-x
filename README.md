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
