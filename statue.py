# setup:1.0 rightwheel blue
# mission7
# by David


from pybricks.tools import run_task, wait, multitask
import careful_recovery
from robot import drive, left_attach


async def statue():
    await drive.straight(290)
    await drive.turn(90)
    await drive.straight(500)
    await drive.turn(-89)
    await left_attach.run_until_stalled(300, duty_limit=20)

    await drive.straight(35)
    await left_attach.run_angle(200, -200)
    await drive.straight(-35)
    await drive.turn(62)
    await drive.straight(290)
    await left_attach.run_angle(200, 200)
    await drive.turn(-60)
    await drive.straight(-250)
    await drive.turn(90)
    drive.settings(straight_speed=800)
    await drive.straight(950)
    # await multitask(drive.straight(50), left_attach.run_angle(200, 50))

    # left_attach.run_time(300, 1000)
    # await drive.straight(-150)
    # await drive.turn(50)
    # drive.settings(straight_speed=800)
    # await drive.straight(800)


if __name__ == "__main__":
    run_task(statue())
