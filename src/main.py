# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       jessestout                                                   #
# 	Created:      11/13/2025, 8:29:14 AM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()
controller = Controller()

ratio = GearSetting.RATIO_6_1

right_motor_front = Motor(Ports.PORT18, ratio, True)
right_motor_back = Motor(Ports.PORT19, ratio, True)
right_motor_top = Motor(Ports.PORT20, ratio, False)
right_drivetrain_motors = MotorGroup(right_motor_front, right_motor_back, right_motor_top)

left_motor_front = Motor(Ports.PORT18, ratio, False)
left_motor_back = Motor(Ports.PORT19, ratio, False)
left_motor_top = Motor(Ports.PORT20, ratio, True)
left_drivetrain_motors = MotorGroup(left_motor_front, left_motor_back, left_motor_top)

drivetrain = DriveTrain(left_drivetrain_motors, right_drivetrain_motors, 300, 320, 320, MM, 3/5)

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    while True:
        wait(20, MSEC)
        drivetrain.drive(FORWARD, controller.axis3.position(), PERCENT)
        drivetrain.turn(LEFT, controller.axis1.position())

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()