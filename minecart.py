# left wheel 1.0
# 9


from pybricks.tools import multitask, run_task, wait
from robot import drive, right_attach


async def minecart():
    await drive.straight(380)
    await drive.turn(36)
    await drive.straight(300)
    await drive.straight(290)
    await drive.turn(15)
    await drive.straight(20)
    await right_attach.run_angle(200, -220)
    await right_attach.run_angle(-200, 220)


if __name__ == "__main__":
    run_task(minecart())
