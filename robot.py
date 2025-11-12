from pybricks.hubs import PrimeHub
from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Port, Direction

hub = PrimeHub()
#Adjust these parameters to fit your robot. Also ensure that you add any sensors here.

left_drive = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_drive = Motor(Port.A, Direction.CLOCKWISE)

left_attach = Motor(Port.C, Direction.CLOCKWISE)
right_attach = Motor(Port.D, Direction.CLOCKWISE)

drive = DriveBase(left_drive, right_drive, 62.4, 135)

#7558, 0, 1889, 4, 7
drive.heading_control.pid(10000, 0, 8000, 3, 7)

drive.use_gyro(True)
