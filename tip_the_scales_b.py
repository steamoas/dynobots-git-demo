# Blue 2.0 left wheel


from pybricks.tools import multitask, run_task, wait
from robot import drive, right_attach, left_attach


async def tip_the_scales_b():
    await drive.straight(160)
    await drive.turn(-85)
    await drive.straight(465)
    await drive.turn(90)

    await drive.straight(83)
    await drive.straight(-120)
    await drive.turn(110)
    drive.settings(straight_speed=500)

    await drive.straight(385)


if __name__ == "__main__":
    run_task(tip_the_scales_b())
