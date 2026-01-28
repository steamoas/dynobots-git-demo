#Blue 2.0 left wheel


from pybricks.tools import multitask, run_task, wait
from robot import drive,right_attach,left_attach

async def tip_the_scales_b():
    await drive.straight(150)
    await drive.turn(-85)
    await drive.straight(465)
    await drive.turn(65)

    await drive.straight(85)
    await drive.straight(-200)
    await drive.turn(110)
    await drive.straight(350)
if __name__ == "__main__":
    run_task(tip_the_scales_b())
