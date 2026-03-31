# setup:1.0 rightwheel blue
# mission7
# by David


from pybricks.tools import run_task, wait
import careful_recovery
from robot import drive, left_attach


async def heavy_lifting():
    await left_attach.run_until_stalled(100, duty_limit=25)
    await left_attach.run_angle(300, -65)
    await drive.straight(100)
    await drive.turn(45)
    await drive.straight(240)
    await drive.turn(-40)
    await drive.straight(400)
    await drive.turn(-22)
    # await left_attach.run_angle(300, -35)
    await drive.straight(150)
    await left_attach.run_angle(300, -100)
    await drive.turn(40)
    await drive.straight(120)
    await drive.turn(-27)
    await drive.straight(-600)
    await drive.turn(-130)
    await drive.straight(320)


if __name__ == "__main__":
    run_task(heavy_lifting())
