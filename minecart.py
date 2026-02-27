# left wheel 1.0
# 9


from pybricks.tools import multitask, run_task, wait
from robot import drive, right_attach


async def minecart():
    await drive.straight(400)
    await drive.turn(40)
    await drive.straight(400)
    await drive.turn(45)
    await drive.straight(150)
    await drive.turn(-70)
    await drive.straight(34)
    await right_attach.run_angle(200, -200)
    await wait(1000)
    await right_attach.run_angle(-200, -200)
    await drive.straight(-200)


if __name__ == "__main__":
    run_task(minecart())
