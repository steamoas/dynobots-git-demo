# left wheel 1.0
# 9


from pybricks.tools import multitask, run_task, wait
from robot import drive, right_attach


async def minecart():
    await drive.straight(400)
    await drive.turn(40)
    await drive.straight(400)
    await drive.turn(45)
    await drive.straight(140)
    await drive.turn(-60)
    await drive.straight(10)
    await right_attach.run_angle(75, -175)
    await wait(2000)
    await drive.straight(-60)
    await drive.turn(-90)
    await drive.straight(100)
    await drive.turn(-90)
    await drive.straight(600)


if __name__ == "__main__":
    run_task(minecart())
