from pybricks.tools import multitask, run_task, wait
from pybricks.parameters import Stop
from robot import drive,right_attach,left_attach

async def run3():
    left_attach.hold()
    drive.settings(straight_speed=600)
    await drive.straight(665)
    await left_attach.run_angle(670,-90)
    await drive.straight(50)
    await left_attach.run_time(100,1000)
    await drive.turn(-55)
 #   await drive.straight(-715)
if __name__ == "__main__":
    run_task(run3())
