# left wheel 1.0
# 9


from pybricks.tools import multitask, run_task, wait
from robot import drive, right_attach


async def minecart():
    await drive.straight(410)
    await drive.turn(30)
    await drive.straight(400)
    await drive.turn(55)
    await drive.straight(150)
    await drive.turn(-65)
    await drive.straight(-15)
    await right_attach.run_angle(50, -200)
    await right_attach.run_angle(700, 175)
    await wait(2000)
    await drive.turn(10)
    await drive.straight(-50)
    await drive.turn(-90)
    await drive.straight(100)
    await drive.turn(-90)
    await drive.straight(600)


if __name__ == "__main__":
    run_task(minecart())
