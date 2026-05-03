# left wheel 1.0
# 9


from pybricks.tools import multitask, run_task, wait
from robot import drive, right_attach


async def minecart():
    await drive.straight(410)
    await drive.turn(30)
    await drive.straight(400)
    await drive.turn(20)
    await drive.straight(65)
    right_attach.run(-110)
    await wait(2050)
    # right_attach.run(100)
    # await  wait(200)
    # await right_attach.run_angle(100, -100)
    # await right_attach.run_angle(230, 130)
    await drive.straight(-450)
    await drive.turn(-40)
    await drive.straight(-350)


if __name__ == "__main__":
    run_task(minecart())
