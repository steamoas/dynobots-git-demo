from pybricks.tools import multitask, run_task, wait
from pybricks.parameters import Stop
from robot import drive, right_attach, left_attach


async def run3():
    left_attach.hold()
    drive.settings(straight_speed=600)
    await drive.straight(665)
    await drive.straight(-200)
    await left_attach.run_angle(670, 130)
    await drive.straight(347)
    # await left_attach.run_time(100, 1000)
    # await drive.turn(90)
    # await left_attach(300, 90)
    # await drive.turn(70)
    # await drive.straight(-200)
    # await drive.turn(50)
    await drive.straight(-50)
    drive.settings(turn_rate=50)
    await drive.turn(90)
    await drive.straight(280)
    await multitask(drive.turn(30), left_attach.run_angle(100, 355), race=False)
    await drive.straight(-330)
    await drive.turn(60)
    await drive.straight(775)


#   await drive.straight(-715)
if __name__ == "__main__":
    run_task(run3())
