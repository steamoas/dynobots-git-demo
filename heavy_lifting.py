# setup:1.0 rightwheel blue
# mission7
# by David


from pybricks.tools import run_task, wait
import careful_recovery
from robot import drive, left_attach


async def heavy_lifting():
    await drive.straight(100)
    await drive.turn(45)
    await drive.straight(250)
    await drive.turn(-40)
    await drive.straight(400)
    await drive.turn(-20)
    await drive.turn()


if __name__ == "__main__":
    run_task(heavy_lifting())
