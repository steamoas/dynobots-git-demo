from pybricks.tools import run_task
from robot import drive,left_attach
async def run2():
#left_attach.run_until_stalled(-100, duty_limit=50);
    await drive.straight(50)
    await drive.curve(62.4,95)
    await drive.straight(400)
    await drive.straight(-150)
    await drive.turn(-90)
    await drive.straight(20)
    await drive.turn(90)
    await drive.straight(250)

if __name__ == "__main__":
    run_task(run2())
