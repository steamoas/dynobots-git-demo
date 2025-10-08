from pybricks.hubs import PrimeHub
from pybricks.robotics import DriveBase
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Port, Direction

hub = PrimeHub()
#Adjust these parameters to fit your robot. Also ensure that you add any sensors here.

left_drive = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_drive = Motor(Port.C, Direction.CLOCKWISE)

left_attach = Motor(Port.A, Direction.CLOCKWISE)
right_attach = Motor(Port.B, Direction.CLOCKWISE)

drive = DriveBase(left_drive, right_drive, 62.4, 118)
drive.use_gyro(True)
