#Blue 2.0 left wheel


from pybricks.tools import multitask, run_task, wait
from robot import drive,right_attach,left_attach

async def tip_the_scales_a():

    drive.settings(straight_speed=400)


    await left_attach.run_until_stalled(300,duty_limit=30)
    await left_attach.run_angle(320,-150)

    await drive.curve(210, 64)

    await drive.straight(690)

    await left_attach.run_time(300, 1000)
    await drive.straight(-150)
    await drive.turn(50)
    drive.settings(straight_speed=800)
    await drive.straight(800)

if __name__ == "__main__":
    run_task(tip_the_scales_a())
