# left wheel 1.0
# 9


from pybricks.tools import multitask, run_task, wait
from robot import drive, right_attach


async def whats_on_sale():
    await drive.straight(250)
    await drive.turn(-54)
    await drive.straight(200)
    await right_attach.run_angle(100, 110)
    await drive.straight(-95)
    await right_attach.run_angle(100, -100)
    await drive.straight(-200)


if __name__ == "__main__":
    run_task(whats_on_sale())
