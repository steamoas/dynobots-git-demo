# left wheel 0.2
# 5,6


from pybricks.tools import multitask, run_task, wait
from robot import drive, right_attach


async def run1():

    await right_attach.run_until_stalled(-300, duty_limit=30)

    await drive.straight(750)

    await right_attach.run_angle(300, 130)
    await multitask(drive.turn(-35), wait(1500), race=True)

    await drive.straight(-750)


if __name__ == "__main__":
    run_task(run1())
