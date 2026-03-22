from pybricks.tools import run_task, wait
from robot import drive, left_attach


async def run2():
    # left_attach.run_until_stalled(-100, duty_limit=50);
    await drive.straight(50)
    await drive.curve(50, 100)

    # await drive.straight(390)
    drive.drive(300, 0)
    await wait(1450)
    await drive.straight(-150)
    await drive.turn(-90)
    await drive.straight(200)
    await drive.turn(90)
    await drive.straight(250)
    drive.settings(straight_speed=400)
    await drive.straight(-850)


if __name__ == "__main__":
    run_task(run2())
