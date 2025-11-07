from pybricks.tools import multitask, run_task, wait
from robot import drive,right_attach,left_attach

async def accross_the_table():
    drive.use_gyro(True)
    drive.heading_control.pid(10000, 0, 8000, 3, 7)
    await drive.straight(200)
    await drive.turn(-90)
    await drive.straight(1675)
if __name__ == "__main__":
    run_task(accross_the_table())
