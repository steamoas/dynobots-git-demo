# setup:1.0 rightwheel blue
# mission7
# by David


from pybricks.tools import run_task, wait
import careful_recovery
from robot import drive, left_attach


async def statue():
    await drive.straight(290)
    await drive.turn(90)
    await drive.straight(500)
    await drive.turn(-90)
    await left_attach.run_until_stalled(300, duty_limit=20)
    await drive.straight(50)
    await left_attach.run_angle(200, -200)


if __name__ == "__main__":
    run_task(statue())
