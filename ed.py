from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase


test
left_drive = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_drive = Motor(Port.A, Direction.CLOCKWISE)

drive = DriveBase(left_drive, right_drive, 60, 100)
drive.use_gyro(True)

drive.curve(-60, -90)
